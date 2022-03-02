from faker import Faker

fake = Faker(locale='en_CA')
advantage_shopping_url = "https://advantageonlineshopping.com/#/"
lbun_length = 5
ubun_length = 15
new_username = fake.user_name()
while True:
    if (len(new_username) >= lbun_length) & (len(new_username) <= ubun_length):
        break
    else:
        new_username = fake.user_name()
email = fake.email()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f"{first_name} {last_name}"
phone_number = fake.phone_number()
country = fake.country()
city = fake.city()
address = fake.street_address()
province = fake.province_abbr()
postal_code = fake.postalcode_in_province()
current_name = new_username
current_password = new_password
subject = fake.sentence(nb_words=20)
