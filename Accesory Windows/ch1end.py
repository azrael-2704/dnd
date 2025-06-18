import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector as sql


ppath = 'D:\\Amartya\'s Files\\XII\\Computer Science\\Project\\Images\\'
wpath = 'D:\\Amartya\'s Files\\XII\\Computer Science\\Project\\Wizard\\'

def wizstr16():

    global wizsc16

    #wizstr5.after(500, lambda: wizstr5.destroy())

    wizsc16 = tk.Toplevel()
    wizsc16.attributes('-fullscreen', True)
    wizsc16.configure(bd = 0)

    wizsc16_can = tk.Canvas(wizsc16, width = 1920, height = 1080, bg = 'black')
    wizsc16_can.pack(expand = True, fill = 'both')
    
    wbg16 = ImageTk.PhotoImage(Image.open('{}Parchment 6.jpg'.format(wpath)))
    wizsc16_can.create_image(0, 0, image = wbg16, anchor = 'nw')

    wizsc16_inv = tk.Button(wizsc16, text = 'Proceed to CH2', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7)
    wizsc16_inv.place(x = 1916, y = 890, anchor = 'ne')

    wizsc16_ext = tk.Button(wizsc16,text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = sqlsc.destroy)
    wizsc16_ext.place(x = 1916, y = 1076, anchor = 'se')

    wizsc16.mainloop()
wizstr16()
