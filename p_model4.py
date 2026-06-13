from pydantic import BaseModel, EmailStr, AnyUrl, field_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin: AnyUrl
    age: int
    weight: float
    marriage: bool = False
    allergies: List[str]
    contact_detail: Dict[str,str]

    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com', 'icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("not a valid domain")
        return value

    @field_validator("name")
    @classmethod
    def name_validator(cls,value):
        return value.upper()
    
    @field_validator("age", mode = "after")
    @classmethod
    def age_validator(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError("age is not valid")

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin)
    print(patient.age)
    print(patient.weight)    
    print(patient.marriage)    
    print(patient.allergies)    
    print(patient.contact_detail)    

    print("This is the data")

patient_info = {"name":"Thor","age": "90","email":"abc@icici.com", "linkedin": "http://linkedin.com/1252", "weight": 75, "allergies":["pollen","dust"],"contact_detail":{"phone_no":"8893938493"}}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)