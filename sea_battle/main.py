# https://www.youtube.com/watch?v=TYkMfZj_Xes&list=PLxiU3nwEQ4PGrVqfHb4DhElHrIeJsFHah&index=5
# from tkinter import *
import random
import time
import tkinter
from tkinter import messagebox

# print(TkVersion)
app_running = True
size_canvas_x = 600
size_canvas_y = 600
s_x = s_y = 10  # number of cell of game field s_y = 12
step_x = size_canvas_x // s_x
step_y = size_canvas_y // s_y
size_canvas_x = step_x * s_x  # correction size_canvas_x
size_canvas_y = step_y * s_y  # correction size_canvas_y
menu_x = 250
ships = s_x // 2  # max number of ships
ship_len1 = s_x // 5  # length 1st type of ship
ship_len2 = s_x // 3  # length 2nd type of ship
ship_len3 = s_x // 2  # length 3rd type of ship
enemy_ships = []
list_ids = []  # list of objects canvas


def on_closing():
    global app_running
    if messagebox.askokcancel("Exit", "Do you want exit from game?"):
        app_running = False
        tk.destroy()


tk = tkinter.Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Sea Battle")
tk.resizable(False, False)
tk.wm_attributes("-topmost", 1)
canvas = tkinter.Canvas(tk, width=size_canvas_x + menu_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
canvas.pack()
tk.update()


# Grid area
def draw_table():
    j: int
    for i in range(0, s_x + 1):
        j = step_x * i
        canvas.create_line(j, 0, j, size_canvas_y, fill="blue")

    for i in range(0, s_y + 1):
        j = step_y * i
        canvas.create_line(0, j, size_canvas_x, j, fill="blue")


draw_table()


# ---
def button_show_enemy():
    print("button_show_enemy")
    generate_enemy_ships()
    global list_ids
    for i in range(s_x):
        for j in range(s_y):
            if enemy_ships[j][i] > 0:
                _id = canvas.create_rectangle(i * step_x, j * step_y,
                                              (i + 1) * step_x, (j + 1) * step_y,
                                              fill="red")
                list_ids.append(_id)


def button_begin_again():
    print("button_begin_again")
    global list_ids
    for i in list_ids:
        canvas.delete(i)
    list_ids = []


b0 = tkinter.Button(tk, text="Show enemy ships", command=button_show_enemy)
b1 = tkinter.Button(tk, text="Begin again", command=button_begin_again)
b0.place(x=size_canvas_x + 20, y=30)
b1.place(x=size_canvas_x + 20, y=70)


# Debug info
def add_to_all(event):
    _type = 0  # LMB
    if event.num == 3:
        _type = 1  # RMB
    # print(_type)

    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    # print(mouse_x, mouse_y)

    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y
    print(_type, ":", ip_x, ip_y)


canvas.bind_all("<Button-1>", add_to_all)  # LMB
canvas.bind_all("<Button-3>", add_to_all)  # RMB


# Place enemy ships
def generate_enemy_ships():
    global enemy_ships
    ships_list = []

    for _ in range(ships):
        ships_list.append(random.choice([ship_len1, ship_len2, ship_len3]))

    sum_1_all_ships = sum(ships_list)
    sum_1_enemy = 0

    while sum_1_enemy != sum_1_all_ships:
        # обнуляем массив кораблей врага
        enemy_ships = [[0 for _ in range(s_x + 1)] for _ in range(s_y + 1)]
        # +1 для доп. линии справа и снизу, для успешных проверок генерации противника

        for i in range(ships):
            len_ship = ships_list[i]
            horizont_vertical = random.randrange(1, 3)  # 1 - горизонтальное 2 - вертикальное

            about_x = random.randrange(0, s_x)
            if about_x + len_ship > s_x:
                about_x = about_x - len_ship

            about_y = random.randrange(0, s_y)
            if about_y + len_ship > s_y:
                about_y = about_y - len_ship

            # print(horizont_vertical, about_x,about_y)
            if horizont_vertical == 1 and about_x + len_ship <= s_x:
                for j in range(len_ship):
                    try:
                        check_near_ships = enemy_ships[about_y][about_x - 1] + \
                                           enemy_ships[about_y][about_x + j] + \
                                           enemy_ships[about_y][about_x + j + 1] + \
                                           enemy_ships[about_y + 1][about_x + j + 1] + \
                                           enemy_ships[about_y - 1][about_x + j + 1] + \
                                           enemy_ships[about_y + 1][about_x + j] + \
                                           enemy_ships[about_y - 1][about_x + j]
                        # print(check_near_ships)
                        if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                            enemy_ships[about_y][about_x + j] = i + 1  # записываем номер корабля
                    except Exception:
                        return

            if horizont_vertical == 2 and about_y + len_ship <= s_y:
                for j in range(len_ship):
                    try:
                        check_near_ships = enemy_ships[about_y - 1][about_x] + \
                                           enemy_ships[about_y + j][about_x] + \
                                           enemy_ships[about_y + j + 1][about_x] + \
                                           enemy_ships[about_y + j + 1][about_x + 1] + \
                                           enemy_ships[about_y + j + 1][about_x - 1] + \
                                           enemy_ships[about_y + j][about_x + 1] + \
                                           enemy_ships[about_y + j][about_x - 1]
                        # print(check_near_ships)
                        if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                            enemy_ships[about_y + j][about_x] = i + 1  # записываем номер корабля
                    except Exception:
                        return

                        # делаем подсчет 1ц
        sum_1_enemy = 0
        for i in range(s_x):
            for j in range(s_y):
                if enemy_ships[j][i] > 0:
                    sum_1_enemy = sum_1_enemy + 1


# generate_enemy_ships()

# App process
while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()

    time.sleep(.005)
