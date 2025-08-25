import joblib
import pandas as pd




def get_data():

    print('Hello! Enter your loan application data and see the result (approved or not approved).')

    data = []


    num_features = ['Age', 'Income', 'Credit score', 'Loan amount', 'Loan term']

    for num_feature in num_features:

        while True:

            value = input(f'{num_feature}: ')

            try:
                value = int(value)
            except ValueError:
                print('Please, enter the number value.')
                continue
            else:
                data.append(value)
                break

            
    while True:

        employment_status = ['Employed', 'Self-Employed', 'Unemployed']

        value = input('Employment status (enter one of these values: Employed, Self-Employed, Unemployed): ')

        if value not in employment_status:
            print('Please, enter one of these values: Employed, Self-Employed, Unemployed)')
        else:
            data.append(value)
            break


    return data





def main():

    print('This app uses a machine learning model to predict loan approval.')

    model = joblib.load('models/random_forest.joblib')
    transformer = joblib.load('models/transformer.joblib')

    data = get_data()

    df = pd.DataFrame(data=[data], columns=['Age', 'Income', 'Credit_Score', 'Loan_Amount',	'Loan_Term', 'Employment_Status'])
    transformed_data = transformer.transform(df)

    loan_approved = model.predict( transformed_data )[0]
    print(f'Loan approved: {"Yes" if loan_approved else "No"}')

    print('Have a nice day!')




if __name__ == '__main__':

    main()


