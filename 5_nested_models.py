from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'street':'123 Main St', 'city':'New York', 'state':'NY', 'zip_code':'10001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'John Doe', 'gender': 'Male', 'age': 30, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.zip_code)


#Better organization of related data (e.g., vitals, address, insurance)

#Reusablitlity: Use vitals in multiple models (e.g. Patient, Medical Record)

#Readability: Easier for developers and API Consumers to understand

#Validation: Nested models are validated automatically-no extra work needed