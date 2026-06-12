from pydantic import BaseModel
# Step 1
class Patient(BaseModel):
    name: str
    age: int
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("This is the data")
# Step 2
patient_info = {"name":"Thor","age": 1990}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)