![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&width=1000&height=200&section=header&text=Natural%20Language%20Processing&fontSize=30&fontColor=black)


<!-- header is made with: https://github.com/kyechan99/capsule-render -->

[Illya Nayshevsky, Ph.D.](http://www.illya.bio) [<img src="https://cdn2.auth0.com/docs/media/connections/linkedin.png" alt="LinkedIn -  Illya Nayshevsky" width=15/>](https://www.linkedin.com/in/illyanayshevskyy/)

<br>
Columbia FinTech Bootcamp Assignment

---

### Table of Contents
* [Overview](#overview)
* [Requirements](#requirements)
* [Data](#data)
* [Sentiment Analysis](#sentiment-analysis)
* [Natural Language Processing](#natural-language-processing)
* [Named Entity Recognition](#named-entity-recognition)

---

## Overview

Natural language processing was used to derive Sentiment Analysis and perform Named Entity Recogntion (NER) on Bitcoin and Ethereum recent news dataset. The analysis returned sentiment analysis in form of positive, negative and neutral sentiment; as well as word

---

## Requirements

A new [conda](https://docs.conda.io/en/latest/) environment and [Jupyter Notebook/Lab](https://jupyter.org/) are requried to run the code.

The following libraries were used:

1. [Natural Language Toolkit (NLTK)](https://www.nltk.org/) - leading platform for building Python programs to work with human language data.
2. [NewsAPI](https://newsapi.org/) - source of articles and breaking news headlines from news sources and blogs across the web
3. [spaCy](https://spacy.io/) - language processing


All of the packages can be installed from terminal:

```python
pip install pandas
pip install python-dotenv
pip install nltk
pip install matplotlib
pip install newsapi-python
pip install -U spacy
python -m spacy download en_core_web_sm
```

Or, can be installed at the point of env creation:
```python
conda create --name <env> --file reqs.txt
```

---

## Data

The data used in language processing analysis was from NewsAPI. 100 Bitcoin and 100 Ethereum articles in English language were taked for analysis:

```python
newsapi.get_everything(q=str<coin name>, language='en', page=int<i>)['articles'] 
# where page corresponds to a multiple of 20 articles (ex. 60 articles :  page=3)
```

---

## Sentiment Analysis


### Method

```python
import nltk as nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
```

### Results
#### Bitcoin

|       | compound | positive | negative | neutral |
|------:|:--------:|:--------:|:--------:|:-------:|
| count |  100.000 |  100.000 |  100.000 | 100.000 |
|  mean |   0.034  |   0.054  |   0.043  |  0.903  |
|   std |   0.408  |   0.068  |   0.052  |  0.079  |
|   min |  -0.763  |   0.000  |   0.000  |  0.677  |
|   25% |  -0.273  |   0.000  |   0.000  |  0.847  |
|   50% |   0.000  |   0.040  |   0.000  |  0.919  |
|   75% |   0.350  |   0.078  |   0.074  |  0.959  |
|   max |   0.846  |   0.282  |   0.203  |  1.000  |


#### Ethereum

|       | compound | positive | negative | neutral |
|------:|:--------:|:--------:|:--------:|:-------:|
| count |  100.000 |  100.000 |  100.000 | 100.000 |
|  mean |   0.093  |   0.060  |   0.036  |  0.894  |
|   std |   0.366  |   0.062  |   0.055  |  0.119  |
|   min |  -0.869  |   0.000  |   0.000  |  0.000  |
|   25% |  -0.178  |   0.000  |   0.000  |  0.851  |
|   50% |   0.000  |   0.058  |   0.000  |  0.921  |
|   75% |   0.402  |   0.097  |   0.069  |  0.954  |
|   max |   0.778  |   0.246  |   0.286  |  1.000  |

---

## Natural Language Processing

```python
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
```

```python
from collections import Counter
from nltk import ngrams
```

### Results
#### Bitcoin

|         tokens        | count |
|:---------------------:|:-----:|
|          (elon, musk) |   27  |
|   (virtual, currency) |   11  |
|   (currency, bitcoin) |   11  |
| (illustration, taken) |   11  |
|       (char, bitcoin) |   9   |
|       (char, reuters) |   9   |
|         (seen, front) |   8   |
|           (ceo, elon) |   7   |
|           (bos, elon) |   7   |
|  (accepting, bitcoin) |   6   |

<img src="img/btc_wc.png" width="60%" self-align="center">

#### Ethereum

|            tokens           | count |
|:---------------------------:|:-----:|
|             (char, bitcoin) |   11  |
|   (expressed, entrepreneur) |   7   |
| (entrepreneur, contributor) |   7   |
|                (elon, musk) |   7   |
|         (virtual, currency) |   6   |
|       (illustration, taken) |   6   |
|            (char, opinions) |   6   |
|       (opinions, expressed) |   6   |
|          (vitalik, buterin) |   5   |
|         (bitcoin, ethereum) |   5   |

<img src="img/eth_wc.png" width="60%" self-align="center">

---

## Named Entity Recognition