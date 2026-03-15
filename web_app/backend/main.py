from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import numpy as np
import joblib
import pandas as pd




app = FastAPI()


class Data(BaseModel):
    gender: Optional[str] = None
    married: Optional[str] = None
    dependents: Optional[str] = None
    education: Optional[str] = None
    self_employed: Optional[str] = None
    applicantincome: Optional[float] = Field(None, ge=0)
    coapplicantincome: Optional[float] = Field(None, ge=0)
    loanamount: Optional[float] = Field(None, ge=0)
    loan_amount_term: Optional[float] = Field(None, ge=0)
    credit_history: Optional[str] = None
    property_area: Optional[str] = None


model = joblib.load('random_forest.joblib')




@app.get('/')
def index():
    return {'status': 'everything is okay'}




@app.post('/get-loan-prediction')
def get_loan_predition(data: Data):

    data = data.model_dump()

    if data['gender'] not in ['male', 'female', None]:
        raise HTTPException(status_code=400, detail="gender must be 'male' or 'female'")
    
    if data['married'] not in ['no', 'yes', None]:
        raise HTTPException(status_code=400, detail="married must be 'yes' or 'no'")
    
    if data['dependents'] not in ['0', '1', '2', '3+', None]:
        raise HTTPException(status_code=400, detail="dependents must be '0', '1', '2', or '3+'")
    
    if data['education'] not in ['not graduate', 'graduate', None]:
        raise HTTPException(status_code=400, detail="education must be 'graduate' or 'not graduate'")
    
    if data['self_employed'] not in ['no', 'yes', None]:
        raise HTTPException(status_code=400, detail="self_employed must be 'yes' or 'no'")
    
    if data['credit_history'] not in ['no', 'yes', None]:
        raise HTTPException(status_code=400, detail="credit_history must be 'yes' or 'no'")
    
    if data['property_area'] not in ['rural', 'urban', 'semiurban', None]:
        raise HTTPException(status_code=400, detail="property_area must be 'rural', 'urban', or 'semiurban'")
    

    data = {k: np.nan if v is None else v for k, v in data.items()}
    data = {key:[value] for key, value in data.items()}
    data = pd.DataFrame(data)

    predition = model.predict(data)[0]
    predition = 'yes' if predition == 1 else 'no'


    return {'predition': predition}



