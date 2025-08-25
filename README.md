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


























