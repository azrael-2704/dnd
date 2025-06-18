import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector as sql


def chrsc_win():

    global chrsc

    chrsc = tk.Tk()
    chrsc.title('Dungeons and Dragons')
    chrsc.geometry('1920x1080')

    chrsc_can = tk.Canvas(chrsc, width = 1920, height = 1080, bg = 'black')
    chrsc_can.pack(expand = True, fill = 'both')

    main_bg = ImageTk.PhotoImage(Image.open('Home Screen BG.jpg'))
    chrsc_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    knt_bg = ImageTk.PhotoImage(Image.open('Knight Cropped.jpg'))
    chrsc_knt = tk.Label(chrsc, padx = 0, pady = 0, relief = 'raised',
                         image = knt_bg, bd=5)
    chrsc_knt.place(x = 10, y = 10, anchor = 'nw')

    mnk_bg = ImageTk.PhotoImage(Image.open('Monk Cropped.jpg'))
    chrsc_mnk = tk.Label(chrsc, padx = 0, pady = 0, relief = 'raised',
                         image = mnk_bg, bd=5)
    chrsc_mnk.place(x = 485, y = 10, anchor = 'nw')

    thf_bg = ImageTk.PhotoImage(Image.open('Thief Cropped.jpg'))
    chrsc_thf = tk.Label(chrsc, padx = 0, pady = 0, relief = 'raised',
                         image = thf_bg, bd=5)
    chrsc_thf.place(x = 960, y = 10, anchor = 'nw')

    wiz_bg = ImageTk.PhotoImage(Image.open('Wizard Cropped.jpg'))
    chrsc_wiz = tk.Label(chrsc, padx = 0, pady = 0, relief = 'raised',
                         image = wiz_bg, bd=5)
    chrsc_wiz.place(x = 1435, y = 10, anchor = 'nw')

    chrsc_knt_btn = tk.Button (chrsc, text = 'KNIGHT', bg = '#272625', 
                               font = ('Enchanted Land', 80), fg = 'white',
                               padx = 40, pady = 5, command = knt_opt)
    chrsc_knt_btn.place(x = 10 , y = 820, anchor = 'nw')

    chrsc_mnk_btn = tk.Button (chrsc, text = 'MONK', bg = '#272625',
                               font = ('Enchanted Land', 80), fg = 'white',
                               padx = 70, pady = 5, command = mnk_opt)
    chrsc_mnk_btn.place(x = 485 , y = 820, anchor = 'nw')

    chrsc_thf_btn = tk.Button (chrsc, text = 'THIEF', bg = '#272625',
                               font = ('Enchanted Land', 80), fg = 'white',
                               padx = 75, pady = 5, command = thf_opt)
    chrsc_thf_btn.place(x = 960 , y = 820, anchor = 'nw')

    chrsc_wiz_btn = tk.Button (chrsc, text = 'WIZARD', bg = '#272625',
                               font = ('Enchanted Land', 80), fg = 'white',
                               padx = 20, pady = 5, command = wiz_opt)
    chrsc_wiz_btn.place(x = 1435 , y = 820, anchor = 'nw')

    chrsc.mainloop()

def knt_opt():

    global opt

    opt = 'knt'


def mnk_opt():

    global opt

    opt = 'mnk'


def thf_opt():

    global opt

    opt = 'thf'
    

def wiz_opt():

    global opt

    opt = 'wiz'

chrsc_win()
