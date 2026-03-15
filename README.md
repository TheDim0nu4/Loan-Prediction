# 💰 Loan Prediction

This project focuses on analyzing data about loan approval and building a machine learning model to predict loan approval based on client information. 
The project includes EDA, preprocessing the data, training machine learning models, then evaluating and comparing their performance. 
It also has a simple web application where a client can enter their data and see the loan result.



## 📁 Project Structure

```
Loan-Prediction/
│
├── data/
│ ├── dataset.csv
│
├── models/
│ ├── logistic_regression.joblib
│ ├── random_forest.joblib
│ ├── svm.joblib
│ ├── xgboost.joblib
│
├── notebooks/
│ ├── eda.ipynb
│ ├── modeling.ipynb
│
├── web_app/
│ ├── backend/
│ ├── frontend/
│ ├── docker-compose.yml
│
├── README.md
├── requirements.txt
```

- data/ folder with data.
- models/ folder with trained models.
- notebooks/ folder with jupyter notebooks.
- web_app/ folder with web application
- README.md provides project overview and instructions.
- requirements.txt specifies Python dependencies.



## 📊 Dataset 

The dataset used is a publicly available dataset from Kaggle called 'Loan Approval Prediction'. The dataset has 614 rows and 13 columns. <br>
 
The columms are: <br>

Loan_ID - a unique loan ID. <br>
Gender - either male or female. <br>
Married - whether the applicant is married (yes) or not married (no). <br>
Dependents - number of people who depend on the applicant. <br>
Education - applicant education (graduate or not graduate). <br>
Self_Employed - whether the applicant is self-employed (Yes/No). <br>
ApplicantIncome - applicant income. <br>
CoapplicantIncome - co-applicant income. <br>
LoanAmount - loan amount in thousands. <br>
Loan_Amount_Term - loan term in months. <br>
Credit_History - whether the credit history meets the guidelines. <br>
Property_Area - where the applicant lives (urban, semi-urban or rural). <br>
Loan_Status - loan approved (y/n). <br>

Source: https://www.kaggle.com/datasets/ssiddharth408/loan-prediction-dataset



## 🔍 Exploratory Data Analysis (EDA)

As a first step, we need to explore and visualize our data. The goal of this step is to understand the data and see what we need to do in the preprocessing step. <br>

It includes: <br>
- Explore basic information about the data (null values and statistics). <br>
- Check the class distribution. <br>
- Create pairplots and a correlation map to see relationships between features. <br>
- Visualize boxplots and value distributions for each attribute. <br>
- Explore how the categorical column – Employment_Status – influences the target attribute. <br>

Graphs and detailed information are available in eda.ipynb



## 🛠️ Data Preprocessing

In this step, we need to preprocess our data based on the EDA. <br>

It includes: <br>
- loading the data. <br>
- train-test split. <br>
- applying a one-hot encoder on the categorical column. <br>
- applying normalization on the numerical columns. <br>
- applying SMOTEEN (a method that combines oversampling and undersampling). <br>
- saving the preprocessed data. <br>

Code and explanation are available in preprocessing.ipynb



## 🤖 Modeling 

In this step, we are going to train some machine learning models. We will train classic models for binary classification like logistic regression and support vector machines. 
We will also train powerful models like random forest and gradient boosting, which work well with non-linear data. For each model, we will use grid search to find the best hyperparameters. <br>

For each model we will do: <br>

1. Define the model and the grid of parameters. <br>
2. Train the model and find the best parameters. <br>
3. Check the best parameters. <br>

Then we will save our models. <br>

Code is available in modeling.ipynb



## 📈 Evaluation 

We already have trained models, so we need to evaluate and compare their performance. We will evaluate each model using a confusion matrix and a classification report 
(it includes important metrics like precision, recall, F1, and accuracy) 

Results for each model are available in evaluation.ipynb



## 🏆 Results

During evaluation, we see that random forest and gradient boosting are almost perfect models, while logistic regression and SVM have a problem with class 1. This can be related to the nature of the data, because in the EDA we saw that the data is non-linear separable, which explains why logistic regression has the worst performance. SVM performs better than logistic regression but still has a problem with class 1. Other algorithms, random forest and gradient boosting, work very well on non-linear data. Credit score, loan amount, and income influence the model decisions the most. In the EDA, in the pairplot and correlation table, we saw that these features stand out from the rest. In conclusion, we can say that machine learning models, especially random forest and gradient boosting, can be used in this field as very helpful tools.



## 🛠️ Tools Used

- Python (Pandas, Matplotlib, Searbon, Scikit-learn, Imbalanced-learn, Joblib)
- Jupyter Notebook



## ⚡ Installation

1. Clone the repository: <br>

   `git clone https://github.com/TheDim0nu4/Loan-Prediction.git` <br>
   `cd Loan-Prediction` <br>
   
2. Create a Python virtual environment (optional but recommended): <br>

   `python -m venv venv` <br>

3. Install the required dependencies: <br>

   `pip install -r requirements.txt` <br>



## ✍️ Author

This project was implemented in the summer of 2025. The project was carried out by Dmytro Skrypchenko.












