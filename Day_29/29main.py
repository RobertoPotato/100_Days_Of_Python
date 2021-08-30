from tkinter import *
def action():
    pass
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
webs_entry.grid(row=1, column=1, columnspan=2)

# EMAIL/USERNAME SECTION
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)

# PASSWORD SECTION
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
pw_entry = Entry(width=52)
pw_entry.grid(row=3, column=1, columnspan=2)
button = Button(text="Generate Password", width=15, highlightthickness=0, command=action)
button.grid(row=3, column=2)

# ADD BUTTON SECTION
button = Button(text="Add", command=action, width=45, )
button.grid(row=4, column=1, columnspan=2)
window.mainloop()
