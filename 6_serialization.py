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

#temp is used to convert model to dictionary
#temp = patient1.model_dump()

temp = patient1.model_dump(include={'address':['city']})

print(temp)
print(type(temp))

