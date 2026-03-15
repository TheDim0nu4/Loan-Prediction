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
- Explore basic information about the data (null values, duplicate rows and statistics). <br>
- Check the class distribution. <br>
- Create pairplots and a correlation map to see relationships between features. <br>
- Visualize boxplots and value distributions for each attribute. <br>
- Explore how the categorical columns influences the target attribute. <br>

Graphs and detailed information are available in eda.ipynb



## 🛠️ Data Preprocessing

In this step, we need to preprocess our data based on the EDA. <br>

It includes: <br>
- loading the data. <br>
- train-test split. <br>
- creating a preprocessing pipeline that handles numerical and categorical features and also applies SMOTE, an oversampling method, to handle class imbalance. <br>

Code and explanation are available in modeling.ipynb



## 🤖 Modeling 

In this step, we are going to train some machine learning models. We will train classic models for binary classification like logistic regression and support vector machines. 
We will also train powerful models like random forest and XGBoost, which work well with non-linear data. For each model, we will use grid search to find the best hyperparameters. <br>

Code is available in modeling.ipynb



## 📈 Evaluation 

After training the models, we need to evaluate and compare their performance. We will evaluate each model using a confusion matrix and a classification report. It includes important metrics such as precision, recall, F1-score, and accuracy. After we identify the best model, we will use cross-validation to check that the model works well with different data distributions and to get a more reliable evaluation of its performance.

Results for each model are available in modeling.ipynb



## 🏆 Results

Four machine learning models were evaluated: logistic regression, SVM, random forest, and XGBoost. The results show that logistic regression and SVM have difficulties correctly predicting class 0, which indicates that simpler models cannot fully capture the patterns in the data. <br>

Among the tested models, random forest achieved the best overall performance, especially in identifying class 0 (recall ≈ 0.58), while maintaining very strong results for class 1. In contrast, XGBoost performed worse for class 0 (recall ≈ 0.50), meaning it tends to predict the majority class more often. <br>

Cross-validation of the best model shows stable performance with an average accuracy around 0.80 and macro F1-score around 0.72, indicating good generalization ability. Feature importance analysis also shows that credit history, loan amount, and income have the strongest influence on model predictions. <br>

Overall, the results suggest that ensemble models, particularly random forest, are the most suitable approach for this loan prediction task.



## 🛠️ Tools Used

- Python (Pandas, Matplotlib, Searbon, Scikit-learn, XGBoost, Imbalanced-learn, Joblib)
- Jupyter Notebook

 For creating a web application:

- FastAPI
- Vue.js
- Docker



## ⚡ Installation

1. Clone the repository: <br>

   `git clone https://github.com/TheDim0nu4/Loan-Prediction.git` <br>
   `cd Loan-Prediction` <br>
   
2. Create a Python virtual environment (optional but recommended): <br>

   `python3.11.1 -m venv venv` <br>

3. Install the required dependencies: <br>

   `pip install -r requirements.txt` <br><br>


To use the web application, you need: <br>

1. Install Docker: <br>

   https://www.docker.com <br>

2. Open the folder with the web application: <br>

   `cd web_app` <br>

3. Run the application using Docker Compose: <br>

   `docker compose up --build` <br>
   
   The application will be available at the URL: http://localhost:5173 <br>

4. To stop the running web application: <br>

   `docker compose down` <br>



## ✍️ Author

The project was carried out by Dmytro Skrypchenko.












