from tkinter import *
import time 
wn = Tk()
wn.title("Digital Clock")
wn.geometry("600x80")
wn.configure(bg="black")
def get_time():
    curr_time = time.strftime("%a, %b %d %Y, %I:%M:%S")
    time_label.config(text=curr_time)
    time_label.after(1000, get_time)
time_label = Label(wn,bg= "black",fg="red", font=("calibri", 39, "bold"))
time_label.pack(anchor="center")
get_time()

wn.mainloop()
