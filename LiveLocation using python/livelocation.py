import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+919550722677")
phone_number2 = phonenumbers.parse("+917993580913")
phone_number3 = phonenumbers.parse("+919640754040")
phone_number4 = phonenumbers.parse("+447774944676")
phone_number5 = phonenumbers.parse("+1(337)842-9956")

print("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_number1, "en"))
print(geocoder.description_for_number(phone_number2, "en"))
print(geocoder.description_for_number(phone_number3, "en"))
print(geocoder.description_for_number(phone_number4, "en"))
print(geocoder.description_for_number(phone_number5, "en"))
