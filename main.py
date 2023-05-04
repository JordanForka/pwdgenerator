import secrets
import string

# necessary imports
import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

pwd_length = int(input("Password Length(only numbers please): "))
amount = int(input("How many passwords to be generated: "))
print("------Generating------")
# generate a password string
for x in range(amount):
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    print(pwd)



