from pydantic import BaseModel, EmailStr, AnyUrl, model_validator, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin: AnyUrl
    age: int
    weight: float
    height: float
    marriage: bool = False
    allergies: List[str]
    contact_detail: Dict[str,str]

    @model_validator(mode = 'after')
    def validate_emergency_contact(cls, BaseModel):
        if BaseModel.age>60 and 'emergency' not in BaseModel.contact_detail:
            raise ValueError("older than 60 must have emergency contact")
        return BaseModel

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin)
    print(patient.age)
    print(patient.weight)    
    print(patient.marriage)    
    print(patient.allergies)    
    print(patient.contact_detail)    
    print("BMI:", patient.bmi)

    print("This is the data")

patient_info = {"name":"Thor","age": "90","email":"abc@icici.com", "linkedin": "http://linkedin.com/1252", "weight": 75,"height":1.72, "allergies":["pollen","dust"],"contact_detail":{"phone_no":"8893938493","emergency":"4748489"}}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)