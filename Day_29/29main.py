from tkinter import *
delimiter = "|"
def action():
    pass
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pwd():
    # key_data = site + delimiter + email + delimiter + pwd + "\n"
    key_data = "site + delimiter + ===========d"
    with open("passwords.txt", 'w') as pwd_file:
        pwd_file.write(key_data)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# LOGO
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# WEBSITE SECTION
webs_label = Label(text="Website:")
webs_label.grid(row=1, column=0)
webs_entry = Entry(width=52)
webs_entry.focus()
webs_entry.grid(row=1, column=1, columnspan=2)

# EMAIL/USERNAME SECTION
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=52)
email_entry.insert(0, "robbs@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

# PASSWORD SECTION
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
pw_entry = Entry(width=52)
pw_entry.grid(row=3, column=1, columnspan=2)
button = Button(text="Generate Password", width=15, highlightthickness=0, command=action)
button.grid(row=3, column=2)
print("PWD: ", pw_entry)

# ADD BUTTON SECTION
button = Button(text="Add", command=save_pwd, width=45, )
button.grid(row=4, column=1, columnspan=2)
window.mainloop()
