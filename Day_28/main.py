from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    lbl_ttl.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if REPS % 2 == 0:
        count_down(short_break_sec)
        lbl_ttl.config(text="Short Break", fg=PINK)
    elif REPS % 8 == 0:
        count_down(long_break_sec)
        lbl_ttl.config(text="Long Break", fg=RED)
    else:
        count_down(work_sec)
        lbl_ttl.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    global REPS
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if int(count_sec) == 0:
        count_sec = "0"
    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

lbl_ttl = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 34, "bold"))
lbl_ttl.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

btn_start = Button(text="Start", highlightthickness=0, command=start_timer)
btn_start.grid(row=2, column=0)
btn_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
btn_reset.grid(row=2, column=2)

check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()
