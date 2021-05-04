import requests


SHEETY_ENDPOINT = "https://api.sheety.co/802ab903566d952628c23c0c93790639/flightDeals/"

print("Welcome to Flight Club \n We find the best deals for you\n")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_confirmed = input("Type your email again\n")

if email != email_confirmed:
    email_confirmed = input("Emails did not match. What is your email?")

email_list = requests.get(url=f"{SHEETY_ENDPOINT}users")
email_response = email_list.json()

all_emails = [item["email"] for item in email_response["users"]]
if email_confirmed in all_emails:
    email_confirmed = input("That email is already in use. Please enter again")



# response = requests.post(
#     url=f"{SHEETY_ENDPOINT}users",
#     json= {
#         "user": {
#             "firstName": first_name,
#             "lastName": last_name,
#             "email": email_confirmed,
#         }
#     })
# response.raise_for_status()