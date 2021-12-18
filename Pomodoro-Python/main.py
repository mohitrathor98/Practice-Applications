import tkinter
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f2cfa7"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    
    # on 0th, 2nd, 4th and 6th rep work
    # on 7th long break
    # else short break
    if reps % 2 == 0:
        timer_label.config(text="Work!", fg=GREEN)
        count_down(5)
    else:
        if reps == 7:
            timer_label.config(text="Break", fg=RED)
            count_down(LONG_BREAK_MIN*60)
        else:
            timer_label.config(text="Break", fg=PINK)
            count_down(2)
    reps+=1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count/60)
    count_sec = count % 60
    
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    
    if count_min <= 9:
        count_min = f"0{count_min}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()
        global reps
        # for every two reps a tick mark should be added
        if reps%2 != 0:
            check.config(text=f"{'✔'*(reps//2)}")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro") # tomato in italian
window.config(padx=100, pady=50, bg=YELLOW)

# timer label
timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

# canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text =canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# start and reset buttons
start = tkinter.Button(text="Start", width=2, bg=YELLOW, command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)

reset = tkinter.Button(text="Reset", width=2, bg=YELLOW, command=reset_timer, highlightthickness=0)
reset.grid(column=2, row=2)

# check
check = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check.grid(column=1, row=3)


window.mainloop()