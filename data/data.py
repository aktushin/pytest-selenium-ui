from faker import Faker

faker = Faker('en_US')


class TextBoxData:
    NAME = faker.name()
    EMAIL = faker.email()
    ADDRESS = faker.address()
