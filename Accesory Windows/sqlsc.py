import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector as sql
from pygame import mixer


# MySQL Connectivity Function #
def mysql_con():

    global con

    con = sql.connect(host = 'localhost', user = 'root', passwd = mysql_pass)
    if con.is_connected:
        confirm_lbl = tk.Label(sqlsc, text='Connection Successful',
                               font=('Bahnschrift SemiBold SemiConden', 12),
                               bg='black', fg='white')
        confirm_lbl.place(x = 50, y = 55, anchor = 'nw')


# Playing Audio Track #
def play_bgm():
    mixer.init()
    mixer.music.load("Main Track 1 Hour.mp3")
    mixer.music.set_volume(0.04)
    mixer.music.play()


# Getting the Password for MySQL #
def get_pass():

    global mysql_pass

    mysql_pass = sqlsc_txtb.get()


## MySQL SCREEN CONNECTOR WINDOW ##
def sqlsc_win():

    global sqlsc_txtb, sqlsc

    sqlsc = tk.Tk()
    sqlsc.title("MySQL Connectivity Gateway")
    sqlsc.geometry('560x100')
    sqlsc.configure(bg = 'black')

    sqlsc_lbl = tk.Label(sqlsc, text = 'Please Enter Your MySQL Password:',
                         font = ('Bahnschrift SemiBold SemiConden', 12),
                         bg = 'black', fg = 'white')
    sqlsc_lbl.place(x = 10, y = 10, anchor = 'nw')

    sqlsc_txtb = tk.Entry(sqlsc, show = '*', width = 20, relief = 'sunken',
                          justify = 'center',  bd = 5,
                          font = ('Bahnschrift SemiBold SemiConden', 12))
    sqlsc_txtb.place(x = 250, y = 10, anchor = 'nw')

    sqlsc_psw = tk.Button(sqlsc, text = 'Store Password',
                          font = ('Bahnschrift SemiBold SemiConden', 12),
                          bg = '#272625', fg = 'white', command = get_pass)
    sqlsc_psw.place(x = 435, y = 10, anchor = 'nw')

    mus_bg = ImageTk.PhotoImage(Image.open('D:\\Amartya\'s Files\\XII\\Computer Science\\Project\\Images\\Music Icon Original.png'))

    sqlsc_mus = tk.Button(sqlsc, image = mus_bg, bg = 'black',
                          bd = 0, command = play_bgm)
    sqlsc_mus.place(x = 550, y = 90, anchor = 'se')

    sqlsc_but = tk.Button(sqlsc, text = 'Check Connection',
                          font = ('Bahnschrift SemiBold SemiConden', 12),
                          bg = '#272625', fg = 'white', command = mysql_con)
    sqlsc_but.place(x = 255, y = 55, anchor = 'nw')

    sqlsc_btn = tk.Button(sqlsc, text = 'Proceed',
                          font = ('Bahnschrift SemiBold SemiConden', 12),
                          bg = '#272625', fg = 'white') #Add Command Here#
    sqlsc_btn.place(x = 385, y = 55, anchor = 'nw')

    sqlsc.mainloop()


sqlsc_win()
