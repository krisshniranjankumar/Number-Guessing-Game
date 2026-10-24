import tkinter as kinder

import random

window = kinder.Tk() #creates a window

window.title("Number Game")

frame = kinder.Frame(window)
frame.pack(pady=75)
window.iconbitmap("game_icon.ico")

window_width = 450

window_height = 350

screen_width = window.winfo_screenwidth()

screen_height = window.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)

center_y = int(screen_height/2 - window_height/2)

window.geometry("{}x{}+{}+{}".format(window_width, window_height, center_x, center_y))

kinder.Label(frame, text="Guess the number (range is 1 to 100): ", font=("Arial",14,"italic")).pack(pady=5)

num = random.randint(1,100)

count = 0

def game(event):
    global count

    try:
        count += 1
        guess = int(num_entry.get())
        
        if num > guess:
            display.config(text="Higher than {}".format(guess))
            num_entry.delete(0,kinder.END)
        elif num < guess:
            display.config(text="Lower than {}".format(guess))
            num_entry.delete(0,kinder.END)
        elif num == guess:
            frame.pack_forget()
            new_frame = kinder.Frame(window)
            new_frame.pack(pady=75)
            kinder.Label(new_frame, text="Victory!", font=("Arial", 20,"bold")).pack()
            kinder.Label(new_frame, text="(you won with {} tries)".format(count), font=("Arial", 12,"italic")).pack()
            def end():
                window.destroy()
            kinder.Button(new_frame, text="End", command=end, font=("Arial",11)).pack(pady=5)
    except ValueError:
        count -= 1
        num_entry.delete(0, kinder.END)
        display.config(text="Please enter a number.")


            
num_entry = kinder.Entry(frame, width=15, font=("Arial",12), justify="center",  relief="solid")
num_entry.pack(pady=5)

num_entry.bind("<Return>", game)

display = kinder.Label(frame, text="", font=("Arial",12))
display.pack(pady=5)

window.resizable(False, False)

window.mainloop()
