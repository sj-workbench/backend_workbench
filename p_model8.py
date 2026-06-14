from fastapi import FastAPI, Path,Query, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
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

class UpdatePatients(BaseModel):
    name: Annotated[Optional[str], Field(default = None)]
    age: Annotated[Optional[int], Field(default = None, gt = 0)]
    weight: Annotated[Optional[float], Field(gt = 0)]
    height: Annotated[Optional[float], Field(gt = 0)]
    gender: Annotated[Optional[Literal['male','female','others']], Field(default = None)]
    city: Annotated[Optional[str], Field(default = None)]
    
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
            return "overweight"
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

@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient_update: UpdatePatients):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code = 404, detail = "Patient not found")
    existing_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset = True)

    for key, value in updated_patient_info.item():
        existing_patient_info[key] = value
    
    existing_patient_info['id'] = patient_id
    patient_pydanitc_obj = Patients(**existing_patient_info)
    existing_patient_info = patient_pydanitc_obj.model_dump(exclude = 'id')
    
    data[patient_id] = existing_patient_info

    save_data(data)
    return JSONResponse(status_code = 200, content = {"message":"patient updated"})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code = 404, detail = 'Patient not found')
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code = 200, content = {"message": "patient deleted"})