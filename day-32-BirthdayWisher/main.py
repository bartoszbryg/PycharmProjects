##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib as smtp
import random

import pandas

hour_to_send_email = 15

data = pandas.read_csv("birthdays.csv")
# dict_with_birthdays = data.to_dict(orient="records")

is_person_sent = []
for _ in range(len(data["name"].tolist())):
    is_person_sent.append(False)

# birthdays_list = []
# for row in dict_with_birthdays:
#     new_time = dt.datetime(year=row["year"], month=row["month"], day=row["day"])
#     birthdays_list.append({"name": row["name"], "email": row["email"], "birth_date": new_time})


#  4. Send the letter generated in step 3 to that person's email address.
def send_email(to_who, email_message):
    my_email = "EMAIL"
    password = "PASSWORD"

    receiver_email = to_who

    with smtp.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver_email,
                            msg=f"Subject: Happy Birthday! \n\n{email_message}")
        print("Email sent!")


# 2. Check if today matches a birthday in the birthdays.csv
while True:
    current_time = dt.datetime.now()
    for index, person in data.iterrows():
        if current_time.day == person["day"] and current_time.month == person["month"] and current_time.hour == hour_to_send_email:
            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
            if not is_person_sent[index - 1]:
                with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as random_letter:
                    text_to_send = ""
                    for line in random_letter:
                        text_to_send += line.replace("[NAME]", person["name"])

                    send_email(person["email"], text_to_send)
                    print(text_to_send)
                    is_person_sent[index - 1] = True
    if current_time.hour == hour_to_send_email+1:
        is_person_sent[index - 1] = False




# current_time = dt.datetime.now()
# for index, person in data.iterrows():
#     if current_time.day == person["day"] and current_time.month == person["month"]:
#         # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
#         with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as random_letter:
#             text_to_send = ""
#             for line in random_letter:
#                 text_to_send += line.replace("[NAME]", person["name"])
#
#             send_email(person["email"], text_to_send)
#             print(text_to_send)




