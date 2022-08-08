import random
from dataclasses import dataclass

from faker import Faker

faker = Faker('en_US')


@dataclass
class TextBoxData:
    department = ['Insurance', 'Compliance', 'Legal', 'Product Decisions', 'Price Decisions']

    FIRST_NAME: str
    LAST_NAME: str
    NAME: str
    EMAIL: str
    AGE: int
    SALARY: int
    ADDRESS: str
    DEPARTMENT: str


input_data = TextBoxData(FIRST_NAME=faker.first_name(),
                         LAST_NAME=faker.last_name(),
                         NAME=faker.name(),
                         EMAIL=faker.email(),
                         AGE=random.randint(0, 60),
                         SALARY=random.randint(5000, 10000),
                         ADDRESS=faker.address(),
                         DEPARTMENT=TextBoxData.department[random.randint(0, 4)])
