import random

from faker import Faker

faker = Faker('en_US')


class InputData:
    department = ['Insurance', 'Compliance', 'Legal', 'Product Decisions', 'Price Decisions']

    FIRST_NAME = faker.first_name()
    LAST_NAME = faker.last_name()
    NAME = faker.name()
    EMAIL = faker.email()
    AGE = random.randint(0, 60)
    SALARY = random.randint(5000, 10000)
    ADDRESS = faker.address()
    DEPARTMENT = department[random.randint(0, 5)]
