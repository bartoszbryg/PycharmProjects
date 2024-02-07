from tkinter import *
from tkinter import messagebox
import math
import random
import pyperclip
import json


# ----------------------- USERNAME AND PASSWORD SEARCHER ------------------------ #


def find_username_and_password():

    # JSON give you the opportunity to access data using one or more keywords (it is like dictionary)
    # ------------ 1st WAY - ACCESS TO JSON FILE (RECOMMENDED!!!) ------------------- #
    website_name = website_entry.get()
    if len(website_name) == 0:
        messagebox.showwarning(title="Warning!", message="Please don't leave field 'Website' empty.")
        return

    try:
        with open("data.json", "r") as data_file:
            login_json_data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="File not found",
                             message="Data File Not Found. You need to enter login details first")

    else:
        if website_name in login_json_data:
            email_name = login_json_data[website_name]["email"]
            password = login_json_data[website_name]["password"]
            messagebox.showinfo(title=f"Login details: {website_name}",
                                message=f"Email/Username: {email_name} \nPassword: {password}")
        else:
            messagebox.showerror(title="Login Data Not Found",
                                 message=f"No details for the website '{website_name}' exists"
                                         f"\nYou need to enter them first")

    # ------------------------------------------------------------------------------- #
    # ------------------------------------------------------------------------------- #
    # ---------------- 2nd WAY - ACCESS TO A PLAIN TXT FILE ------------------------- #
    # website_name = website_entry.get()
    # if len(website_name) == 0:
    #     messagebox.showwarning(title="Warning!", message="Please don't leave field 'Website:' empty.")
    #     return
    # webpages = []
    # try:
    #     with open("data.txt") as file_data:
    #         for line in file_data:
    #             words = line.split(" | ")
    #             webpages.append(words[0])
    #             if line.startswith(website_name):  # words[0] == website_name:
    #                 messagebox.showinfo(title=f"Login details: {website_name}",
    #                                     message=f"Email/Username: {words[1]} \nPassword: {words[2]}")
    #
    #         if website_name not in webpages:
    #             messagebox.showerror(title="Login Data Not Found",
    #                                  message=f"No details for the website '{website_name}' exists")
    # except FileNotFoundError:
    #     messagebox.showerror(title="File not found",
    #                          message="Data File not found. You need to enter login details first!")
    # ----------------------------------------------------------------------------------- #
    # ----------------------------------------------------------------------------------- #


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    organized_password_list = []
    random_password = ""

    # for _ in range(random.randint(7, 10)):
    #     organized_password_list.append(random.choice(letters))
    # for _ in range(random.randint(3, 6)):
    #     organized_password_list.append(random.choice(numbers))
    # for _ in range(random.randint(3, 6)):
    #     organized_password_list.append(random.choice(symbols))

    letters = [random.choice(letters) for _ in range(random.randint(7, 10))]
    numbers = [random.choice(numbers) for _ in range(random.randint(3, 6))]
    symbols = [random.choice(symbols) for _ in range(random.randint(3, 6))]

    organized_password_list = letters + numbers + symbols

    # BEST MY OWN SOLUTION WITHOUT SHUFFLE !!!
    # ---------------------------------------------
    # while len(organized_password_list) > 0:
    #     random_char = random.choice(organized_password_list)
    #     random_password += random_char
    #     organized_password_list.remove(random_char)
    # ---------------------------------------------

    random.shuffle(organized_password_list)

    for char in organized_password_list:
        random_password += char

    password_entry.delete(0, END)
    password_entry.insert(0, random_password)
    pyperclip.copy(password_entry.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    name_of_website = website_entry.get()
    email_name = email_entry.get()
    password = password_entry.get()

    if len(name_of_website) == 0 or len(email_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning!", message="Please don't leave any fields empty!")
    # elif "@" not in email_name:
    #     messagebox.showwarning(title="Warning!", message="Your email should contain @")
    else:
        should_save = messagebox.askyesnocancel("Make sure", f"You have entered the following data:\n"
                                                             f"Name of website: {name_of_website}\n"
                                                             f"Email/Username: {email_name}\nPassword: {password}\n"

                                                             f"Are you sure you want to save the above data?")
        if should_save:
            # ---------------- 1nd WAY - SAVING TO JSON FILE (RECOMMENDED!!!) ------------------- #
            # ----------------------------------------------------------------------------------- #
            new_data = {
                # e.g. new bird name (sth which will identify particular content)
                name_of_website: {
                    # e.g. color of bird and other details which we can access using the identifier like bird name
                    # (in this case the identifier is the name_of_website)
                    "email": email_name,
                    "password": password
                }
            }
            # new_data IS THE DICTIONARY, BUT IF WE UPDATE IT TO JSON FILE, THE CONTENT WILL BECOME NEW KEY VALUE

            #  WRONG !!! IT CREATES MULTIPLE DICTIONARIES THAT WE DON'T WANT - WE CAN'T USE 'a' OPERATING ON JSON FILES
            # with open("data.json", "a") as data_file:
            #     json.dump(new_data, data_file, indent=4)

            try:

                with open("data.json", "r") as data_file:
                    # Reading old data and saving them to the dictionary
                    json_data = json.load(data_file)
                    print(type(json_data))

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # Updating old data with new data
                json_data.update(new_data)
                print(json_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(json_data, data_file, indent=4)

            # ---------------------------------------------------------------------------------- #
            # ---------------------------------------------------------------------------------- #
            # ----------------- 2st WAY - SAVING TO A PLAIN TEXT FILE -------------------------- #
            # with open("data.txt", "a") as data_file:
            #     data_file.write(f"{name_of_website} | {email_name} | {password}\n")
            # ---------------------------------------------------------------------------------- #
            # ---------------------------------------------------------------------------------- #

            # finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# USING STICKY !!! ADAPTING SIZE TO ONE OR MORE OBJECTS
# USING COLUMNSPAN !!! STRETCH BY A SPECIFIED NUMBER OF COLUMNS/ROWS
# USING PADDING !!! THE DISTANCE BETWEEN PARTICULAR OBJECTS


root = Tk()
root.title("Password Manager")
root.config(padx=70, pady=70)

canvas = Canvas(root, width=150, height=180)
canvas.grid(column=1, row=0)

logo_image = PhotoImage(file="logo.png")
canvas.create_image(math.floor(canvas.winfo_reqwidth() / 2) - 2, math.floor(canvas.winfo_reqheight() / 2) - 2,
                    image=logo_image)

website_lab = Label(root, text="Website:")
website_lab.grid(column=0, row=1)  # sticky=E)

email_lab = Label(root, text="Email/Username:")
email_lab.grid(column=0, row=2, padx=20)  # row=2, sticky=E)

password_lab = Label(root, text="Password:")
password_lab.grid(column=0, row=3)  # sticky=E)

website_entry = Entry(root)
website_entry.grid(column=1, row=1, sticky=EW, pady=3)

email_entry = Entry(root)
email_entry.grid(column=1, row=2, columnspan=2, sticky=EW, pady=3)

password_entry = Entry(root)
password_entry.grid(column=1, row=3, sticky=EW, pady=3)

search_button = Button(root, text="Search", command=find_username_and_password)  # width=12)
search_button.grid(column=2, row=1, padx=(10, 0), sticky=EW)

generate_new_pass = Button(root, text="Generate", width=12, command=generate_password)
generate_new_pass.grid(column=2, row=3, padx=(10, 0))

add_button = Button(root, text="Add", command=save_data)
add_button.grid(column=1, columnspan=2, row=4, sticky=EW, pady=3)

# STICKY ADAPTING OBJECTS TO THE BIGGEST OBJECT IN PARTICULAR COLUMN !!!!!
# ---------------------------------------------------------------------------
# STICKY IN COLUMN ONE ADAPTS OBJECTS TO CANVAS WHICH IS THE BIGGEST
# STICKY IN COLUMN TWO ADAPTS OBJECTS TO GENERATE BUTTON WHICH IS THE BIGGEST

root.mainloop()
