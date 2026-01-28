from pydantic import BaseModel, EmailStr, AnyUrl, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float #kg
    height: float #mt
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print('BMI', patient.bmi)
    print(patient.allergies)
    print(patient.contact_details)
    print('update')

patient_info = {'name':'nishant', 'age':66, 'email':'rushi@hdfc.com', 'linked_url':'http://rushi.linkedin.com','weight': 200.29,'height':1.73, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'53252335235','emergency':'323424542'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)