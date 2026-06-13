# Nested Model
from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    pincode: str
    state: str

class Patient(BaseModel):
    name: str
    age: int = Field(strict=True)
    gender: str ='M'
    address: Address 

address_dict = {"city": "wakanda", "state":"usa","pincode": "15262"}
address1 = Address(**address_dict)

patient_dict = {"name": "antman","age": 26,"gender": "M","address": address1}
patient1 = Patient(**patient_dict)
print(patient1)
print(patient1.name)
print(patient1.address.pincode)

# Serialization
# 1
dict_format1 = patient1.model_dump()
print(dict_format1)
print(type(dict_format1))
# 2
dict_format2 = patient1.model_dump_json()
print(dict_format2)
print(type(dict_format2))
# 3
dict_format3 = patient1.model_dump(include = ['name','gender'])
print(dict_format3)
print(type(dict_format3))
# 4
dict_format4 = patient1.model_dump(exclude = ['name','gender'])
print(dict_format4)
print(type(dict_format4))
# 5
dict_format5 = patient1.model_dump(include = {"address":["state"]})
print(dict_format5)
print(type(dict_format5))
# 6
dict_format6 = patient1.model_dump(exclude_unset = True)
print(dict_format6)
print(type(dict_format6))