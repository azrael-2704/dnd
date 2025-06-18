import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector as sql
from pygame import mixer

ppath = 'D:\\Amartya\'s Files\\XII\\Computer Science\\Project\\Images\\'
kpath = 'D:\\Amartya\'s Files\\XII\\Computer Science\\Project\\Knight\\'
mpath = 'D:\\Amartya\'s Files\\XII\\Computer Science\\Project\\Monk\\'
tpath = 'D:\\Amartya\'s Files\\XII\\Computer Science\\Project\\Thief\\'
wpath = 'D:\\Amartya\'s Files\\XII\\Computer Science\\Project\\Wizard\\'

def inventory():

    global invsc

    invsc = tk.Tk()
    invsc.geometry('1280x720')
    
    invsc_can = tk.Canvas(invsc, width = 1920, height = 1080, bg='black')
    invsc_can.pack(expand = True, fill = 'both')

    main_bg = ImageTk.PhotoImage(Image.open('{}Home Screen BG.jpg'.format(ppath)))
    invsc_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    delete = ImageTk.PhotoImage(Image.open('{}Delete.png'.format(ppath)))

    invsc_fr1 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr1.place(x = 100, y = 100, anchor = 'nw')
    invsc_fr1.propagate(0)

    invsc_fr1_1 = tk.Frame(invsc_fr1, width = 400, height = 100, bd = 0)
    invsc_fr1_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr1_1.propagate(0)

    invsc_l1 = tk.Label(invsc_fr1_1, font = ('Enchanted Land', 50, 'bold'),
                        text = 'Sample',
                        bg = '#342D25', fg = 'white')
    invsc_l1.pack(fill = 'both', expand = True)

    invsc_b1 = tk.Button(invsc_fr1, image = delete, bd = 0)
    invsc_b1.pack(side = 'right')

    invsc_fr2 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr2.place(x = 100, y = 205, anchor = 'nw')
    invsc_fr2.propagate(0)

    invsc_fr2_1 = tk.Frame(invsc_fr2, width = 400, height = 100, bd = 0)
    invsc_fr2_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr2_1.propagate(0)

    invsc_l2 = tk.Label(invsc_fr2_1, font = ('Enchanted Land', 50, 'bold'),
                        text = 'Sample',
                        bg = '#342D25', fg = 'white')
    invsc_l2.pack(fill = 'both', expand = True)

    invsc_b2 = tk.Button(invsc_fr2, image = delete, bd = 0)
    invsc_b2.pack(side = 'right')

    invsc_fr3 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr3.place(x = 100, y = 310, anchor = 'nw')
    invsc_fr3.propagate(0)

    invsc_fr3_1 = tk.Frame(invsc_fr3, width = 400, height = 100, bd = 0)
    invsc_fr3_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr3_1.propagate(0)

    invsc_l3 = tk.Label(invsc_fr3_1, font = ('Enchanted Land', 50, 'bold'),
                        text = 'Sample',
                        bg = '#342D25', fg = 'white')
    invsc_l3.pack(fill = 'both', expand = True)

    invsc_b3 = tk.Button(invsc_fr3, image = delete, bd = 0)
    invsc_b3.pack(side = 'right')

    invsc_fr4 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr4.place(x = 100, y = 415, anchor = 'nw')
    invsc_fr4.propagate(0)

    invsc_fr4_1 = tk.Frame(invsc_fr4, width = 400, height = 100, bd = 0)
    invsc_fr4_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr4_1.propagate(0)

    invsc_l4 = tk.Label(invsc_fr4_1, font = ('Enchanted Land', 50, 'bold'),
                        text = 'Sample',
                        bg = '#342D25', fg = 'white')
    invsc_l4.pack(fill = 'both', expand = True)

    invsc_b4 = tk.Button(invsc_fr4, image = delete, bd = 0)
    invsc_b4.pack(side = 'right')

    invsc_fr5 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr5.place(x = 100, y = 520, anchor = 'nw')
    invsc_fr5.propagate(0)

    invsc_fr5_1 = tk.Frame(invsc_fr5, width = 400, height = 100, bd = 0)
    invsc_fr5_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr5_1.propagate(0)

    invsc_l5 = tk.Label(invsc_fr5_1, font = ('Enchanted Land', 50, 'bold'),
                        text = 'Sample',
                        bg = '#342D25', fg = 'white')
    invsc_l5.pack(fill = 'both', expand = True)

    invsc_b5 = tk.Button(invsc_fr5, image = delete, bd = 0)
    invsc_b5.pack(side = 'right')

    invsc_fr6 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr6.place(x = 1180, y = 100, anchor = 'ne')
    invsc_fr6.propagate(0)

    invsc_fr6_1 = tk.Frame(invsc_fr6, width = 400, height = 100, bd = 0)
    invsc_fr6_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr6_1.propagate(0)

    invsc_l6 = tk.Label(invsc_fr6_1, font = ('Enchanted Land', 50, 'bold'),
                        text = 'Sample',
                        bg = '#342D25', fg = 'white')
    invsc_l6.pack(fill = 'both', expand = True)

    invsc_b6 = tk.Button(invsc_fr6, image = delete, bd = 0)
    invsc_b6.pack(side = 'right')

    invsc_fr7 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr7.place(x = 1180, y = 205, anchor = 'ne')
    invsc_fr7.propagate(0)

    invsc_fr7_1 = tk.Frame(invsc_fr7, width = 400, height = 100, bd = 0)
    invsc_fr7_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr7_1.propagate(0)

    invsc_l7 = tk.Label(invsc_fr7_1, font = ('Enchanted Land', 50, 'bold'),
                        text = 'Sample',
                        bg = '#342D25', fg = 'white')
    invsc_l7.pack(fill = 'both', expand = True)

    invsc_b7 = tk.Button(invsc_fr7, image = delete, bd = 0)
    invsc_b7.pack(side = 'right')

    invsc_fr8 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr8.place(x = 1180, y = 310, anchor = 'ne')
    invsc_fr8.propagate(0)

    invsc_fr8_1 = tk.Frame(invsc_fr8, width = 400, height = 100, bd = 0)
    invsc_fr8_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr8_1.propagate(0)

    invsc_l8 = tk.Label(invsc_fr8_1, font = ('Enchanted Land', 50, 'bold'),
                        text = 'Sample',
                        bg = '#342D25', fg = 'white')
    invsc_l8.pack(fill = 'both', expand = True)

    invsc_b8 = tk.Button(invsc_fr8, image = delete, bd = 0)
    invsc_b8.pack(side = 'right')

    invsc_fr9 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr9.place(x = 1180, y = 415, anchor = 'ne')
    invsc_fr9.propagate(0)

    invsc_fr9_1 = tk.Frame(invsc_fr9, width = 400, height = 100, bd = 0)
    invsc_fr9_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr9_1.propagate(0)

    invsc_l9 = tk.Label(invsc_fr9_1, font = ('Enchanted Land', 50, 'bold'),
                        text = 'Sample',
                        bg = '#342D25', fg = 'white')
    invsc_l9.pack(fill = 'both', expand = True)

    invsc_b9 = tk.Button(invsc_fr9, image = delete, bd = 0)
    invsc_b9.pack(side = 'right')

    invsc_fr10 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr10.place(x = 1180, y = 520, anchor = 'ne')
    invsc_fr10.propagate(0)

    invsc_fr10_1 = tk.Frame(invsc_fr10, width = 400, height = 100, bd = 0)
    invsc_fr10_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr10_1.propagate(0)

    invsc_l10 = tk.Label(invsc_fr10_1, font = ('Enchanted Land', 50, 'bold'),
                        text = 'Sample',
                        bg = '#342D25', fg = 'white')
    invsc_l10.pack(fill = 'both', expand = True)

    invsc_b10 = tk.Button(invsc_fr10, image = delete, bd = 0)
    invsc_b10.pack(side = 'right')
        
    invsc.mainloop()

inventory()
