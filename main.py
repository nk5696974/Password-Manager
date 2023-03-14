from tkinter import * 
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbol = [choice(numbers) for _ in range(nr_symbols)]
    password_number = [choice(symbols) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbol + password_number

    shuffle(password_list)

    password = "".join(password_list)
    password_Entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = web_Entry.get()
    email = email_Entry.get()
    password = password_Entry.get()
    new_data = {
        web : {
            "email" : email,
            "password" : password
        }
    }
    
    if (len(web)==0 or len(email) == 0 or len(password) == 0):
        messagebox.showinfo(title="Title", message="You left some fields empty.")
    else:
        try:
            with open("data.json", "r") as file:
                #reading old data
                data = json.load(file)
        except:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:  
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_Entry.delete(0, END)
            email_Entry.delete(0, END)
            password_Entry.delete(0, END)

#------------------------------- FIND PASSWORD -------------------------------#

def find_password():
    try:
        with open("data.json", "r") as file:
            #reading old data
            data = json.load(file)
    except:
        messagebox.showinfo(title="Missing file.", message=f"file not found")
    else:
        mailpassword = {}
        if web_Entry.get() in data:
            mailpassword = data[web_Entry.get()]
            email = mailpassword["email"]
            password = mailpassword["password"]
            messagebox.showinfo(title=f"{web_Entry.get()}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Invalid input", message=f"Entered web is not present.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.iconbitmap(r'password_ico.ico')

#Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

#website label
web_Label = Label(text="Website: ", font=("Railway", 15))
web_Label.grid(row=1, column=0)

#email label
email_Label = Label(text="Email/Username: ", font=("Railway", 15))
email_Label.grid(row=2, column=0)

#password label
password_Label = Label(text="Password: ", font=("Railway", 15))
password_Label.grid(row=3, column=0)

#web entry 
web_Entry = Entry(width=30)
web_Entry.focus()
web_Entry.grid(row=1, column=1, columnspan=2, sticky=W)

#emial Entry
email_Entry = Entry(width=50)
email_Entry.insert(0, "nk5696974@gmail.com")
email_Entry.grid(row=2, column=1, columnspan=2, sticky=W)

#password Entry
password_Entry = Entry(width=25)
password_Entry.grid(row=3, column=1, sticky=W)

#generate password button
generateButton = Button(text="Generate Password", font=("Railway", 10, "bold"), command=generate_password)
generateButton.grid(row=3, column=2)

#Add button
addButton = Button(text="Add", font=("Railway", 10, "bold"), width=35, command=save)
addButton.grid(row=4, column=1, columnspan=2, sticky=W)

#Search button
searchButton = Button(text="Search", font=("Railway", 10, "bold"), width=15, command=find_password)
searchButton.grid(row=1, column=2, sticky=W)

window.mainloop()
