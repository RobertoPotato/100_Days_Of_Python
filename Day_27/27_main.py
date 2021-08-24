from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# Entry
m_input = Entry(width=10)
m_input.pack()


# Button
def button_clicked():
    print("I Got Clicked")
    my_label.config(text=f"{m_input.get()}")


button = Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()
