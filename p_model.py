# 1
def insert_patient_data(name, age):
    print(name)
    print(age)
    print("This is the data")
insert_patient_data("SJ","Thirty")
# 2
def insert_patient_data(name: str, age: int):
    print(name)
    print(age)
    print("This is the data")
insert_patient_data("SJ",30)
# 3
def insert_patient_data(name: str, age: int):
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print("This is the data")
    else:
        raise TypeError("Wrong data")
insert_patient_data("SJ","30")
# 4
def insert_patient_data(name: str, age: int):
    if age<0:
        raise ValueError("age cant be negative")
    else:
        print(name)
        print(age)
        print("This is the data")
insert_patient_data("SJ",-30)
