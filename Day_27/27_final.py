from tkinter import *


# Conversion logic
def mile_to_km():
    km = float(entry_miles.get()) * 1.609
    lbl_ans.config(text=f"{km}")


# Creating the window
window = Tk()
window.title("Mile to KM converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Creating the widgets and conversion logic
entry_miles = Entry(width=10)
lbl_ans = Label(text="-")
lbl_is_eq_to = Label(text="Is Equal To")
lbl_miles = Label(text="Miles")
lbl_km = Label(text="KM")

lbl_cal = Button(text="Calculate", command=mile_to_km)
# Adding the widgets to the window using the grid system
lbl_is_eq_to.grid(row=1, column=0)
entry_miles.grid(row=0, column=1)
lbl_ans.grid(row=1, column=1)
lbl_cal.grid(row=2, column=1)
lbl_miles.grid(row=0, column=2)
lbl_km.grid(row=1, column=2)

window.mainloop()
