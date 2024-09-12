from faker import Faker
import random

class RandomUser:
    def __init__(self):
        self.faker = Faker()
        self.username = self.faker.user_name()
        self.email = self.faker.email()
        self.password = self.faker.password(length=10)
        self.birth_day = str(random.randint(1, 31))
        self.birth_month = str(random.randint(1, 12))
        self.birth_year = str(random.randint(1950, 2005))
        self.first_name = self.faker.first_name()
        self.last_name = self.faker.last_name()
        self.company_name = self.faker.company()
        self.address = self.faker.street_address()
        self.address2 = self.faker.secondary_address()
        self.country = random.choice(["India", "United States", "Israel", "Canada", "Australia", "New Zealand", "Singapore"])
        self.state = self.faker.state()
        self.city = self.faker.city()
        self.zipcode = self.faker.zipcode()
        self.mobile_number = self.faker.phone_number()

        self.random_subject=" ".join(self.faker.words(nb=2))
        self.random_message=" ".join(self.faker.paragraph(nb_sentences=3))

        self.card_number = self.faker.credit_card_number()
        self.card_cvc = self.faker.credit_card_security_code()
        self.expiration_month = str(random.randint(1, 12)).zfill(2)
        self.expiration_year = str(random.randint(24, 30))

    @property
    def card_name(self):
        return f"{self.first_name} {self.last_name}"