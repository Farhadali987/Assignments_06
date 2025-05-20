class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("age must be 18 or older")

try:
    print(check_age(20))
    print(check_age(15))
except InvalidAgeError as e:
    print("Exception",e)