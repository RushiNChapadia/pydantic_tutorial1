from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    # field validator for email
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # adbsasd@gmai.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid email domain')
        return value
    
    # field validator for name
    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()
    
    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


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

patient_info = {'name':'nishant', 'age':30, 'email':'rushi@hdfc.com', 'linked_url':'http://rushi.linkedin.com','weight': 200.29, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'53252335235'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)