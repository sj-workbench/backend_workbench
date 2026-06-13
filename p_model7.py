from fastapi import FastAPI, Path,Query, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

app = FastAPI()

def load_data():
    with open("patients.json",'r') as f:
        data = json.load(f)
    return data
def save_data(data):
    with open("patients.json",'w') as f:
        json.dump(data, f)


class Patients(BaseModel):
    id: Annotated[str, Field(..., description = "ID of the patient", examples = ["P001"])]
    name: Annotated[str, Field(..., description = "Name of the patient")]
    age: Annotated[int, Field(..., gt = 0, lt=120, description = "Age of the patient")]
    weight: Annotated[float, Field(..., gt=0, description = 'Weight of the patient in kgs')]
    height: Annotated[float, Field(..., gt=0, description = 'Height of the patient in mtrs')]
    gender: Annotated[Literal['male','female','others'], Field(..., description = "Gender of the patient")]
    city: Annotated[str, Field(..., description = "Where the patient lives")]
    
    # BMI
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight /(self.height**2),2)
        return bmi

    # Verdict
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "underweight"
        elif self.bmi < 25:
            return "normal"
        elif self.bmi < 30:
            return "normal"
        else:
            return "obese"

# Endpoints
@app.post ("/create")
def create_patient(patient: Patients):

    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code = 400, detail="Patient already exists")

    data[patient.id] = patient.model_dump(exclude= ["id"])

    save_data(data)
    return JSONResponse(status_code = 201, content = {"message":'Patient created successfully'})