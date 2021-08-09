# Import dependencies
import subprocess, os, time
import json
from dotenv import load_dotenv

# Load and set environment variables
load_dotenv("resources/mnemonic.env")
mnemonic = os.getenv("mnemonic")
# print(f"Mnemonic : \"{mnemonic}\"")

# Import constants.py and necessary functions from bit and web3
from constants import *
from bit.wallet import PrivateKeyTestnet, NetworkAPI
from web3 import Account, Web3, HTTPProvider 

# Create a function called `derive_wallets`
def derive_wallets(coin : str,
                   mnemonic : str = mnemonic,
                   numderive : int = 3):
    
    print(mnemonic)
    command = f"./derive -g --mnemonic={str(mnemonic)} --coin={coin} --numderive={str(numderive)} --cols=address,index,path,privkey,pubkey,pubkeyhash,xprv,xpub --format=json"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    print(output)
    return json.loads(output)


# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {}
def populate_coins_dict():
    coins[BTCTEST] = derive_wallets(mnemonic=mnemonic, coin=BTCTEST)
    coins[ETH] = derive_wallets(mnemonic=mnemonic, coin=ETH)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin : str,
                       priv_key : str):
    '''Converts the privkey string in a child key to an account object 
    that bit or web3.py can use to transact'''
        
    if coin == "btc-test":
        return PrivateKeyTestnet(priv_key)
    
    elif coin == "eth":
        return Account.privateKeyToAccount(priv_key)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(acc, 
              coin : str,
              to : str,
              amount : float or int,
              gas : int = 1):
    '''Creates the raw, unsigned transaction that contains all metadata 
        needed to transact'''
    
    if coin == "btc-test":
        return PrivateKeyTestnet.prepare_transaction(acc.address, [(to, amount*100000000, 'usd')])
    
    elif coin == "eth":
        return {'to': to,
                'from' : str(acc.address),
                'value': w3.toWei(amount,'ether'),
                'gas': int(w3.eth.gasPrice / 100000),
                'gasPrice': w3.eth.gasPrice,
                'nonce': w3.eth.getTransactionCount(acc.address),
                'chainId': w3.eth.chainId
                }
        
        
# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(account, 
            coin : str,
            to : str,
            amount : float or int,
            gas : int = 1):
    
    raw_tx = create_tx(acc=account,
                       coin=coin,
                       to=to,
                       amount=amount,
                       gas=gas)
    
    if coin == "btc-test":
        # Sign the transaction with your new wallet private key
        signed = account.sign_transaction(raw_tx)
        
        # Transmit the transaction
        NetworkAPI.broadcast_tx_testnet(signed)
        print(f"{amount} tBTC sent from : {account.address} to : {to}")
    
    elif coin == "eth":
        # Sign the transaction with your new wallet private key
        signed = account.sign_transaction(raw_tx)
        
        # Transmit the transaction
        w3.eth.sendRawTransaction(signed.rawTransaction)
        print(f"{w3.fromWei(amount, 'ether')} eth sent from : {account.address} to : {to}") 
        print(f"Signed transaction : {signed.rawTransaction.hex()}")
        print(f"Signed transaction hash : {signed.hash.hex()}")