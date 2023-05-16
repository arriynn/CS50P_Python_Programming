from validator_collection import validators

email_address= input("what's your email address? ")
try:
    if validators.email(email_address):
        print("Valid")

except:
    print("Invalid")