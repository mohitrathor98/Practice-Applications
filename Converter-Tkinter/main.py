from tkinter import *
from tkinter import messagebox

def calculate():
    miles = miles_input.get()
    try:
        miles = int(miles)
        km = miles*1.60934
        result_label.config(text=f"{round(km)}")
        
    except:
        print("Input Error")
        show_warning = getattr(messagebox, 'show{}'.format('warning'))
        show_warning("Input Error", f"{miles} is not valid input")
        


window = Tk() # creates window
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20) # adding a padding of 20x20 in window 


# text input
miles_input = Entry(width=10)
miles_input.focus()
miles_input.place(x=130, y=20)

# miles label
miles_label = Label(text="Miles", font=("Verdana", 14))
miles_label.place(x=220, y=20)

# is equal to label
equal_label = Label(text="is equal to", font=("Veradana", 14))
equal_label.place(x=10, y=60)

# result label
result_label = Label(text="0", width=10, anchor=CENTER, font=(14))
result_label.place(x=130, y=60)

# km label
km_label = Label(text="Km", font=("Verdana", 14))
km_label.place(x=220, y=60)

# calculate button
button = Button(text="Calculate", command=calculate)
button.place(x=130, y=100)

window.mainloop() # keeps window open