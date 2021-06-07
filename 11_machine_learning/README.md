![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&width=1000&height=200&section=header&text=Machine%20Learning%20-%20Classification&fontSize=30&fontColor=black)

<!-- header is made with: https://github.com/kyechan99/capsule-render -->

[Illya Nayshevsky, Ph.D.](http://www.illya.bio) [<img src="https://cdn2.auth0.com/docs/media/connections/linkedin.png" alt="LinkedIn -  Illya Nayshevsky" width=15/>](https://www.linkedin.com/in/illyanayshevskyy/)

<br>
Columbia FinTech Bootcamp Assignment

---

### Table of Contents
* [Overview](#overview)
* [Requirements](#requirements)
* [Data](#data)
* [Re-sampling](#re-sampling)
* [Ensemble Learning](#ensemble-learning)


---

## Overview

This exercise predicts credit risk with machine learning techniques. 

### Re-sampling

Historically, loan data is imbalanced, with far more loan approvals than rejections. This imbalance stems from the low applicant rejection rates which are believed to be caused by applicant's due diligence prior to loan application. Basically, people apply to loans that they think they will get. The imbalance in the data creates a problem in machine learning, where a model which is trained on imbalanced data will overwhelmingly predict the most probable outcome, neglecting the criteria of negative outcomes completely.

This issue is addressed by re-sampling, where over under-sampling samples the majority class of the dataset, while oversampling copies the minority class, both of which methods create equal weighed classes.  

![underoversampling](https://miro.medium.com/max/725/1*H6XodlitlGDl9YdbwaZLMw.png)

*Source: [Analystic Vidhya](https://www.analyticsvidhya.com/blog/2020/07/10-techniques-to-deal-with-class-imbalance-in-machine-learning/)*

### Learning Models

The learning models used in this exercise are: [Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression) and [Random Forest](https://en.wikipedia.org/wiki/Random_fores).

#### Logistic Regression

Logistic Regression model is used to model probability of events with binary outcomes. The model outcome is a sigmoid, the classification is performed via a threshold. Passing the threshold value classifies the training value either as Pass (1) or Fail (0).

<img src="img/logit.png" width=70%>
 
#### Random Forest 

Random Forest model constructs a multitude of decision trees at training time and outputs a the mode (classification) or the mean (regression) of the individual trees. Random Forest model corrects the over-fitting problem in machine learning. The training data passes through *n*-number of "Trees", returning weighed classes, upon which the final classification is made.

<img src="img/randomforest.png" width=70%>

### Ensemble Learners

[Ensemble learning](https://en.wikipedia.org/wiki/Ensemble_learning) is a machine learning process that utilizes multiple models in order to optimize learning results. Ensemble learners use classifier algorithms, that are strategically arranged in order to increase learning rate, accuracy or precision, compared to using those algorithms alone.

---

## Requirements

Latest version of [Anaconda](https://www.anaconda.com/products/individual) or [Conda](https://docs.conda.io/en/latest/) are required. [Jupyter Notebook](https://jupyter.org/) or [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/) must be installed.


```python
numpy==1.20.2 
pandas==1.2.4 

# scikit-learn : machine learning in python; predictive data analysis
scikit-learn==0.24.2 

# imbalanced-learn : provides tools when dealing with classification with imbalanced classes
imbalanced-learn==0.8.0 
```

### Installing requirements

All requirements for this assignment can be installed in a conda environment, along with other requirements for other CU FinTech assignments.

It is important to create a new conda enviroment prior to installing requirements from <code>requirements.txt</code> file, in order to preserve the current requirements in your <code>(base)</code> environment.

Creating a new environmental and installing requirements can be done in one step:

```python
conda create --name <env> --file requirements.txt
```

If you already have an environment that you prefer to use, you can install the requirements into that environment like this:

```python
conda install --file requirements.txt
```

---

## Data

Analytical data was provided, and was sourced from LendingClub.
Data was prepared in similar was for both [Credit Risk Resampling](#credit-risk-resampling) and [Credit Risk Ensemble](#credit-risk-ensemble) machine learning methods.

### Data preparation

1. Encoding non-numerical data - create columns and fill binary

```python
# get non-numerical data types
list(df_data_types[df_data_types.iloc[:,0] != 'float64'].index)

# beatification of non-numerical data
pd.get_dummies(df : pd.DataFrame, columns : list)
```

2. <code>X</code> and <code>y</code> split - independent and dependent variables

3. Train/test split (75/25 split)

```python
from sklearn.model_selection import train_test_split

# train_test_split returns train/test X: pd.DataFrame and y: pd.Series 
train_test_split(X : pd.DataFrame , y : pd.Series, random_state : int)
```

4. Scaling data - standardize features by removing the mean and scaling to unit variance

```python
from sklearn.preprocessing import StandardScaler

# Create instance and fit the scaler
scaler = StandardScaler()
X_scaler = scaler.fit(X_train : pd.DataFrame)

# apply StandardScaler() to scale the data
X_train_scaled = X_scaler.transform(X_train : pd.DataFrame)
X_test_scaled = X_scaler.transform(X_test : pd.DataFrame)
```

The scaler has produced a normalized X training and testing datasets.

---

## Re-sampling

Re-sampling was performed on [<code>lending_data.csv</code>](Resources/lending_data.csv.csv) data. The calculations were performed in the [<code>credit_risk_resampling.ipynb</code>](credit_risk_resampling.ipynb) notebook.

Re-sampling can be achieved via <code>imbalanced-learn</code> library, which provides a variety of tools for handling imbalanced datasets :  

* Oversampling:
    * <code>RandomOverSampler</code>
    * <code>SMOTE</code>

* Undersampling:
    * <code>ClusterCentroids</code>

* Over/Under-sampling
    * <code>SMOTEEN</code>

### Oversampling
#### RandomOverSampler

[RandomOverSampler()](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.RandomOverSampler.html) randomly over-samples the minority class.

```python
from imblearn.over_sampling import RandomOverSampler

# instantiate oversample
X_resampled, y_resampled = RandomOverSampler(random_state=random_state).fit_resample(X_train_scaled,y_train)
```

#### SMOTE

[SMOTE()](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html) (Synthetic Minority Over-sampling Technique), originally published in 2002 [Journal of Artificial Intelligence Research 16 (2002) 321–357](https://arxiv.org/pdf/1106.1813.pdf), creates synthetic data from minority samples through K-nearest neighbors.

```python
from imblearn.over_sampling import SMOTE

# instantiate oversampler
X_resampled, y_resampled = SMOTE(random_state=random_state).fit_resample(X_train_scaled,y_train)
```

### Under-sampling
#### ClusterCentroids

[ClusterCentroids()](https://imbalanced-learn.org/stable/references/generated/imblearn.under_sampling.ClusterCentroids.html) under-sample the majority class by replacing a cluster of majority samples by the cluster centroid of a KMeans algorithm. [K-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) is a method of vector quantization.

```python
from imblearn.under_sampling import ClusterCentroids

# instantiate oversample
X_resampled, y_resampled = ClusterCentroids(random_state=random_state).fit_resample(X_train_scaled,y_train)
```

### Over/Under-sampling
#### SMOTEEN

[SMOTEENN()](https://imbalanced-learn.org/stable/references/generated/imblearn.combine.SMOTEENN.html) combines over/under-sampling using SMOTE and Edited Nearest Neighbors. [Edited Nearest Neighbors](https://machinelearningmastery.com/undersampling-algorithms-for-imbalanced-classification/) is an under-sampling algorithm.

```python
from imblearn.under_sampling import SMOTEENN

# instantiate oversampler
X_resampled, y_resampled = SMOTEENN(random_state=random_state).fit_resample(X_train_scaled,y_train)
```

### Results


|          Re-sampling type         |        Method       | Balanced acc. score | f1-score | geo. mean | 0 : Pred 0 | 1 : Pred 1 | 0 : Pred 1 | 1 : Pred 0 |
|:---------------------------------:|:-------------------:|:-------------------:|:--------:|:---------:|:----------:|:----------:|:----------:|:----------:|
| None                              | N/A                 |        0.9880       |   0.99   |    0.99   |     581    |    18690   |     11     |     102    |
| Naive Random Oversampling         | RandomOverSampler() |        0.994        |   0.99   |    0.99   |    55915   |    55901   |     329    |     343    |
| SMOTE Oversampling                | SMOTE()             |        0.9945       |   0.99   |    0.99   |    55973   |    55898   |     271    |     346    |
| Undersampling                     | ClusterCentroids()  |        0.9358       |   0.94   |    0.93   |    1891    |    1680    |     17     |     228    |
| Combination (Over/Under)-Sampling | SMOTEEN()           |        0.9983       |   1.00   |    1.00   |    55174   |    55856   |     174    |     11     |

The results have shown that SMOTEENN over/under-sampling is the best way to classify predicts credit risk data. 

Although training a Logistic Regression model using imbalanced data produced the fewest false positives, the imbalanced produced a bias. Under-sampling has also produced a small number of false positives, which was caused due to weighing of the true negatives in the dataset. Combination over/under-sampling has produced the best results proportional to the dataset positive and negative classes, and resulted in the best f1-score and geometric mean.

---

## Ensemble Learning

Ensable learning was performed on [<code>LoanStats</code>](Resources/LoanStats_2019Q1.csv) data. The calculations were performed in the [<code>credit_risk_ensemble.ipynb</code>](credit_risk_ensemble.ipynb) notebook. 


### Credit risk prediction 

In this study, <code>loan_status</code> was predicted based on a multitude of other loan applicant criteria. The possible outcomes were binary: <code>high_risk</code> or <code>low_risk</code>. 

Two types of ensemble learners were utilized, and their results were compared. Both are a part of the **imbalanced-learn** library.

1. [BalancedRandomForestClassfier()](https://imbalanced-learn.org/stable/references/generated/imblearn.ensemble.BalancedRandomForestClassifier.html) : a balanced random forest classifier - randomly under-samples data to balance it.
2. [EasyEnsembleClassifier()](https://imbalanced-learn.org/stable/references/generated/imblearn.ensemble.EasyEnsembleClassifier.html) : an ensemble of [Adaptive Boosting](https://en.wikipedia.org/wiki/AdaBoost) (AdaBoost) learners - randomly under-samples data to balance it.

### Balanced Random Forest Classfier

For production run, the <code>n_estimators</code> was wet to 5000 iterations. For reproducibility, the same <code>random_state</code> value was used for all tests.

After [data preparation]("#data"), the ensemble classifier was instantiated and fitted:

```python
from imblearn.ensemble import BalancedRandomForestClassfier
brf = BalancedRandomForestClassfier(n_estimators : int, random_state :  int)
model = brf.fit(X_train_scaled : pd.DataFrame, y_train : pd.Series)
```

The scaled X test data was then passed to the mode:

```python
y_pred = model.predict(X_test_scaled : pd.DataFrame)
```

Balanced Random Forest Classifier has returned the following results:


> Balanced Accuracy = <code>0.787</code>

> Confusion Matrix:

|   | Pred-0 | Pred-1 |
|--:|-------:|-------:|
| **0** |  15556 |   1545 |
| **1** |     35 |     69 |

> *f1* score = <code>0.95</code>

> *geometric mean* score = <code>0.78</code>


### Easy Ensemble Classifier

After [data preparation]("#data"), the ensemble classifier was instantiated and fitted:

```python
from imblearn.ensemble import EasyEnsembleClassifier
eec = EasyEnsembleClassifier(n_estimators : int, random_state :  int)
model = eec.fit(X_train_scaled : pd.DataFrame, y_train : pd.Series)
```

The scaled X test data was then passed to the mode:

```python
y_pred = model.predict(X_test_scaled : pd.DataFrame)
```

Easy Ensemble Classifier has returned the following results:

> Balanced Accuracy = <code>0.919</code>

> Confusion Matrix:

|   | Pred-0 | Pred-1 |
|--:|-------:|-------:|
| **0** |  16152 |   949 |
| **1** |     11 |     93 |

> *f1* score = <code>0.97</code>

> *geometric mean* score = <code>0.92</code>

### Results 

|                                   | Balanced acc. score | geo. mean | f1-score | 0 : Pred 0 | 1 : Pred 1 | 0 : Pred 1 | 1 : Pred 0 |
|-----------------------------------|:-------------------:|:---------:|:--------:|:----------:|:----------:|:----------:|:----------:|
| Balanced Random Forest Classifier |        0.787        |    0.78   |   0.95   |    15556   |     69     |    1545    |     35     |
| Easy Ensemble Classifier          |        0.919        |    0.92   |   0.97   |    16152   |     93     |     949    |     11     |


Comparing Balanced Random Forest Classifier to Easy Ensemble Classifier, it is evident that the latter has outperformed. Easy Ensemble Classifier Balanced Accuracy Score was 16.7% higher than the score produced by Balanced Random Forest Classifier, 0.787 and 0.919 point respectively. <code>BalancedRandomForest()</code> has also produced 62% greater amount of false positives (<code>0 : Pred 1</code>), and 218% more false negatives (<code>1 : Pred 0</code>). The *f1*-score produced by the <code>BalancedRandomForestClassifier()</code> was also 2% lower than that of <code>EasyEnsambleClassifier()</code>.
