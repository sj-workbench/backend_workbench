from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length = 50, title = "Name of the patient", description = "Give me the name", examples = ['Ironman','CaptainAmerica'])]
    email: EmailStr
    linkedin: AnyUrl
    age: int = Field(gt=0,lt=100)
    weight: float = Field(gt = 0,strict=True)
    marriage: Annotated[bool, Field(default = False,description = "marriage_status")]
    allergies: Optional[List[str]] = None
    contact_detail: Dict[str,str]


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

patient_info = {"name":"Thor","age": 90,"email":"abc@mail.com", "linkedin": "http://linkedin.com/1252", "weight": 75, "allergies":["pollen","dust"],"contact_detail":{"phone_no":"8893938493"}}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)