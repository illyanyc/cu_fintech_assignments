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


---

## Requirements


---

## Data


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