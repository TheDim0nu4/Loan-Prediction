# Loan Prediction

This project focuses on analyzing data about loan approval and building a machine learning model to predict loan approval based on client information. 
The project includes EDA, preprocessing the data, training machine learning models, then evaluating and comparing their performance. 
It also has a simple console application where a client can enter their own data and see the loan result.



## Project Structure

```
📂 Loan-Prediction/
│
├── 📂 data/
│ ├── 📂 processed/
│ │ ├── 📄 train.csv
│ │ ├── 📄 test.csv
│ ├── 📄 loan_prediction.csv
│
├── 📂 models/
│ ├── 📄 gradient_boosting.joblib
│ ├── 📄 logistic_regression.joblib
│ ├── 📄 random_forest.joblib
│ ├── 📄 svm.joblib
│ ├── 📄 transformer.joblib
│
├── 📂 notebooks/
│ ├── 📄 eda.ipynb
│ ├── 📄 evaluation.ipynb
│ ├── 📄 modeling.ipynb
│ ├── 📄 preprocessing.ipynb
│
├── 📄 README.md
├── 📄 app.py
├── 📄 requirements.txt
```

- data/ folder with raw and processed data.
- models/ folder with trained models and the transformer for data preprocessing.
- notebooks/ folder with jupyter notebooks.
- README.md provides project overview and instructions.
- app.py consol application for using model
- requirements.txt specifies Python dependencies



## Dataset 

The dataset used is a publicly available dataset from Kaggle called 'Loan Prediction Dataset'. The dataset has 2000 rows and 7 columns. <br>
 
The columms are: <br>

Age - age of the client. <br>
Income - annual income of the client. <br>
Credit_Score - credit history of the client (a high value means a good history, a low value means the opposite). <br>
Loan_Amount - loan amount that the client wants to get. <br>
Loan_Term - loan term requested by the client. <br>
Employment_Status - employed, self-employed, or unemployed. <br>
Loan_Approved - target attribute, 1 - loan was approved, 2 - loan was not approved. <br>

Source: https://www.kaggle.com/datasets/mosaadhendam/loan-prediction-dataset



## Exploratory Data Analysis (EDA)

As a first step, we need to explore and visualize our data. The goal of this step is to understand the data and see what we need to do in the preprocessing step. <br>

It includes: <br>
- Explore basic information about the data (null values and statistics). <br>
- Check the class distribution. <br>
- Create pairplots and a correlation map to see relationships between features. <br>
- Visualize boxplots and value distributions for each attribute. <br>
- Explore how the categorical column – Employment_Status – influences the target attribute. <br>

Graphs and detailed information are available in eda.ipynb



## Data Preprocessing

In this step, we need to preprocess our data based on the EDA. <br>

It includes: <br>
- loading the data. <br>
- train-test split. <br>
- applying a one-hot encoder on the categorical column. <br>
- applying normalization on the numerical columns. <br>
- applying SMOTEEN (a method that combines oversampling and undersampling). <br>
- saving the preprocessed data. <br>

Code and explanation are available in preprocessing.ipynb



## Modeling 

In this step, we are going to train some machine learning models. We will train classic models for binary classification like logistic regression and support vector machines. 
We will also train powerful models like random forest and gradient boosting, which work well with non-linear data. For each model, we will use grid search to find the best hyperparameters. <br>

For each model we will do: <br>

1. Define the model and the grid of parameters. <br>
2. Train the model and find the best parameters. <br>
3. Check the best parameters. <br>

Then we will save our models. <br>

Code is available in modeling.ipynb



## Evaluation 

We already have trained models, so we need to evaluate and compare their performance. We will evaluate each model using a confusion matrix and a classification report 
(it includes important metrics like precision, recall, F1, and accuracy) 

Results for each model are available in evaluation.ipynb



## Conclusion




















