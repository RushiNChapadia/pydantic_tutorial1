from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of patient', description='Give the name of the patient', examples=['Nitish','Amit'])]
    age: int
    email: EmailStr
    linked_url: AnyUrl
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str,str]

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('insert')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('update')

patient_info = {'name':'nishant', 'age':30, 'email':'rushi@gmail.com', 'linked_url':'http://rushi.linkedin.com','weight': 200.29, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'53252335235'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)