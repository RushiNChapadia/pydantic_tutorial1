from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('update')

patient_info = {'name':'nishant', 'age':66, 'email':'rushi@hdfc.com', 'linked_url':'http://rushi.linkedin.com','weight': 200.29, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'53252335235','emergency':'323424542'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)