# https://www.youtube.com/watch?v=TYkMfZj_Xes&list=PLxiU3nwEQ4PGrVqfHb4DhElHrIeJsFHah&index=2
from tkinter import *
from tkinter import messagebox
import time

# print(TkVersion)
app_running = True
size_canvas_x = 600
size_canvas_y = 600
s_x = s_y = 10  # size of game field
step_x = size_canvas_x // s_x
step_y = size_canvas_y // s_y

# Correction
size_canvas_x = step_x * s_x
size_canvas_y = step_y * s_y

menu_x = 250


def on_closing():
    global app_running
    if messagebox.askokcancel("Exit", "Do you want exit from game?"):
        app_running = False
        tk.destroy()


tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Sea Battle")
tk.resizable(False, False)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x + menu_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="yellow")
canvas.pack()
tk.update()


# Grid area
def draw_table():
    j: int
    for i in range(0, s_x + 1):
        j = step_x * i
        canvas.create_line(j, 0, j, size_canvas_y, fill="red")

    for i in range(0, s_y + 1):
        j = step_y * i
        canvas.create_line(0, j, size_canvas_x, j, fill="blue")


draw_table()


# ---
def button_show_enemy():
    pass


def button_begin_again():
    pass


b0 = Button(tk, text="Show enemy ships", command=button_show_enemy)
b1 = Button(tk, text="Begin again", command=button_begin_again)
b0.place(x=size_canvas_x + 20, y=30)
b1.place(x=size_canvas_x + 20, y=60)


# ---
def add_to_all(event):
    _type = 0  # LMB
    if event.num == 3:
        _type = 1  # RMB

    print(_type)


canvas.bind_all("<Button-1>", add_to_all)  # LMB
canvas.bind_all("<Button-3>", add_to_all)  # RMB


# App process
while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()

    time.sleep(.005)
