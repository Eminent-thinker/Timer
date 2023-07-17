from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
  
def start_timer():
    try:
      count_down(300)
    except:
       pass
def count_down(count):
    minutes = int(count // 60)
    seconds = int(count % 60)
    canvas.itemconfigure(create_text, text = "{:02d}:{:02d}". format(minutes, seconds))
    if count >0:
       global timer
       timer = canvas.after(1000, count_down, count-1)

def pause_timer():
    try:
      canvas.after_cancel(timer)
    except:
        tkinter.messagebox.showwarning("Warning", "You cannot pause the timer")
def reset_timer(count =300):
      try:
        canvas.after_cancel(timer)
        minutes = int(count // 60)
        seconds = int(count % 60)
        canvas.itemconfigure(create_text, text = "{:02d}:{:02d}". format(minutes, seconds))
      except:
           tkinter.messagebox.showerror("Error", "You cannot reset the timer")

root = Tk()
root.title( "Timer")
root.configure(pady = 300, padx = 10)
canvas = Canvas(width = 700, height = 570, bg = 'yellow', highlightthickness = 0)
canvas.grid(row=0, column =0, rowspan = 3, columnspan = 3)
photo = ImageTk.PhotoImage(Image.open("Tomato.jpg"))
canvas.create_image(300,255, image = photo)
timer_label = Label(text = 'Timer', font = ( 'Courier', 14, 'bold'), bg = 'white')
create_text = canvas.create_text(330, 275, text = "00:00", fill = 'white',font = ('Verdana', 16, 'bold'))
start_button = Button(text = "Start", highlightthickness = 0, command = start_timer)
reset_button = Button(text = 'Reset', highlightthickness = 0, command = reset_timer)
pause_button = Button(text = 'Pause', highlightthickness = 0, command = pause_timer)
start_button.grid(row = 2, column = 0)
reset_button.grid(row = 2, column = 2)
pause_button.grid(row = 2, column = 1)
timer_label.grid(row = 0, column = 1)
mainloop()