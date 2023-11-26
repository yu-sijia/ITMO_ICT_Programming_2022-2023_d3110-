import tkinter as tk
import tkinter.messagebox
import threading
import copy

ROWS = 40  
COLS = 40  
SPACE = 10  
root = tk.Tk()
root.title('жизнь')
root.geometry('{}{}{}'.format(ROWS * 10, 'x', COLS * 10))
list_live = [[0 for i in range(ROWS)] for j in range(COLS)]  
isSetOver = False  
a1 = tk.Canvas(root, width=ROWS * 10, height=COLS * 10)


def drawMap():  
    global list_live
    global a1
    for i in range(ROWS):
        for j in range(COLS):
            if list_live[i][j] == 0:
                a1.create_rectangle(i * SPACE, j * SPACE, i * SPACE + SPACE, j * SPACE + SPACE, fill='black',
                                    outline='grey', width=3)
            else:
                a1.create_rectangle(i * SPACE, j * SPACE, i * SPACE + SPACE, j * SPACE + SPACE, fill='white',
                                    outline='grey', width=3)


def callback(event):  
    global isSetOver
    global list_live
    x = event.x / SPACE
    y = event.y / SPACE
    i = int(x)
    j = int(y)
    if isSetOver == False:  
        list_live[i][j] = 1
        a1.create_rectangle(i * SPACE, j * SPACE, i * SPACE + SPACE, j * SPACE + SPACE, fill='white', outline='grey',
                            width=3)
        if i == 0 and j == 0:
            isSetOver = True


a1.bind("<Button-1>", callback)  


drawMap()  
tk.messagebox.showinfo('намекать', "规则1：如果细胞周围有3个存活的细胞 存活\n规则2：如果细胞周围有2个存活的细胞 维持不变\n规则3：其他情况 死亡\n点击(0,0)坐标结束设置并开启自动机")

a1.pack()


def getRoundLive(i, j): 
    num = 0
    global list_live

    if i > 0 and j > 0 and list_live[i - 1][j - 1] == 1: num += 1
    if i > 0 and list_live[i - 1][j] == 1: num += 1
    if i > 0 and j < COLS - 1 and list_live[i - 1][j + 1] == 1: num += 1
    if j > 0 and list_live[i][j - 1] == 1: num += 1
    if j < COLS - 1 and list_live[i][j + 1] == 1: num += 1
    if j > 0 and i < ROWS - 1 and list_live[i + 1][j - 1] == 1: num += 1
    if i < ROWS - 1 and list_live[i + 1][j] == 1: num += 1
    if i < ROWS - 1 and j < COLS - 1 and list_live[i + 1][j + 1] == 1: num += 1

    return num  


def life_week():
    num = 0
    global list_live
    list_now = [[0 for i in range(ROWS)] for j in range(COLS)]
    for i in range(ROWS):
        for j in range(COLS):
            num = getRoundLive(i, j)  
            if 3 == num:
                list_now[i][j] = 1
            elif 2 == num:
                list_now[i][j] = list_live[i][j]
            else:
                list_now[i][j] = 0

    list_live = copy.deepcopy(list_now)  


def my_mainloop():
    root.after(1000, my_mainloop)
    if isSetOver:
        life_week() 
        drawMap()  


root.after(100, my_mainloop())  
root.mainloop()
