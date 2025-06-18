import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector as sql


def lodsc_win():

    global lodsc

    #playsc.after(500, lambda: playsc.destroy())

    lodsc = tk.Tk()
    lodsc.title('Dungeons and Dragons')
    lodsc.geometry('1920x1080')

    lodsc_can = tk.Canvas(lodsc, width = 1920, height = 1080, bg = 'black')
    lodsc_can.pack(expand = True, fill = 'both')

    main_bg = ImageTk.PhotoImage(Image.open('Home Screen BG.jpg'))
    lodsc_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    lodsc_head = tk.Label(lodsc, text = 'Please Enter Player Name', padx = 10,
                          font = ('Enchanted Land', 70), pady = 5,
                          fg = 'white', bg = '#0F0F0F', relief = 'ridge', bd = 5)
    lodsc_head.place(x = 570, y = 410, anchor = 's')

    lodsc_name = tk.Entry(lodsc, font = ('Enchanted Land', 70),
                          width = 20, bd = 7, relief = 'sunken', justify = 'center')
    lodsc_name.place(x= 1225, y = 407, anchor = 's')

    lodsc_sto = tk.Button(lodsc, text = 'OK', bg = '#272625', fg = 'white', padx = 5,
                          font = ('Enchanted Land', 50))
    lodsc_sto.place(x = 1600, y = 410, anchor = 's')

    lodsc_lod = tk.Button(lodsc, text = 'Load Game',
                          font = ('Enchanted Land', 70),
                          bg = '#272625', fg = 'white', padx = 5)
    lodsc_lod.place(x = 950, y = 600, anchor = 'e')

    lodsc_gdm = tk.Button(lodsc, text = 'God Mode',
                          font = ('Enchanted Land', 70),
                          bg = '#272625', fg = 'white', padx = 5)
    lodsc_gdm.place(x = 970, y = 600, anchor = 'w')

    lodsc.mainloop()

    
lodsc_win()
