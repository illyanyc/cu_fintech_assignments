# PyBank - Homework

*a Python script for analyzing the financial records of a company* [Ref. 1][1]

by Illya Nayshevsky

---

## Table to Contents
 - [General Info](#general-info)
 - [Installation](#installation)
 - [Usage](#usage)


## General Info
PyBank is a homework activity assigned by [Columbia University FinTech Bootcamp](https://bootcamp.cvn.columbia.edu/fintech/). The python script analyzes a CSV file with the budget data of the company and returns a summary of the analysis. The summary can be printed to the terminal or saves as a text file.

The analysis summary consists of [Ref. 1][1]:

> - The total number of months included in the dataset.
> - The net total amount of Profit/Losses over the entire period.
> - The average of the changes in Profit/Losses over the entire period.
> - The greatest increase in profits (date and amount) over the entire period.
> - The greatest decrease in losses (date and amount) over the entire period.

## Installation
### General
Latest version of [Anaconda](https://www.anaconda.com/) and Python 3.7 are required to run the script.

Anaconda can be installed by downloading the latest version of the software from [Anaconda.com Downloads](https://www.anaconda.com/products/individual) and installing it locally.


### Libraries
The python native libraries required to run the script are:
1. [csv](https://docs.python.org/3/library/csv.html)
2. Path module from [pathlib](https://docs.python.org/3/library/pathlib.html)

The 3rd party library required to run the script is:
[Pandas](https://pandas.pydata.org/), a data analysis library.

Pandas can be installed with [pip](https://pip.pypa.io/en/stable/):

```python
pip install pandas
```

## Usage
### Preparing the data for analysis
- Data for analysis must be prepared in CSV format
- The following colums are required:
1. Date column: 
    - Column name: <code>"Date"</code> 
    - Data type: date (MM/DD/YYYY)
    - Column index: <code>0</code>
    - Each entery must correspond to one (1) month
2. Profit and Losses column:
    - Column name: <code>"Profit/Losses"</code> 
    - Data type: int or float
    - Column index: <code>1</code>
    - Each entery must be the cumulative profits and losses for the corresponding month

- Header must be present in the CSV file, with corresponding column names

### Setting file paths
- The input file must be in CSV format. The input file name must be set before running the script:

```python
INPUT_FILENAME = Path("../../budget_data.csv")
```

- The output file can be in any text format supported by Python csv module (e.g. .csv, .txt). The output file name should be set to desired file and directory prior to running the script. The output file name defaults to <code>"budget_data_result.txt"</code>:

```python
OUTPUT_FILENAME = Path("budget_data_result.txt")
```

### Loading data
- The data will be loaded via <code>pandas.read_csv()</code> method and written to a Pandas DataFrame for further analysis

### Methods
- All supporting methods are housed in the Methods section of the python notebook.
- Description of each method is available in the method's Docstring.

### Results
- The results are computed by calling the supporting methods and passing the Pandas Dataframe housing all the data into those supporting methods
- The summary of the result is therefore written to a text file, with the file name specified in the [Setting file paths](#setting-file-paths) section.
- The summary of the results is finally printed to the terminal.


[1]: https://columbia.bootcampcontent.com/columbia-bootcamp/cu-nyc-virt-fin-pt-03-2021-u-c/-/tree/master/02-Homework/02-Python/Instructions "Unit 2 | Homework Assignment: Automate Your Day Job with Python; GitLab; Accessed Apr. 2, 2021"