import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector as sql

ppath = 'D:\\Amartya\'s Files\\XII\\Computer Science\\Project\\Images\\'
wpath = 'D:\\Amartya\'s Files\\XII\\Computer Science\\Project\\Wizard\\'


def story():
    
    global root

    #chrsc.after(500, lambda: chrsc.destroy())

    root = tk.Toplevel()
    root.attributes('-fullscreen', True)
    root.configure(bd = 0)

    root_can = tk.Canvas(root, width = 1920, height = 1080, bg = 'black')
    root_can.pack(expand = True, fill = 'both')
    
    main_bg = ImageTk.PhotoImage(Image.open('{}Parchment 1.jpg'.format(wpath)))
    root_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    lbl = tk.Label(root, text = 'Welcome {}!'.format('amartya'),
                   font = ('Enchanted Land', 100, 'bold'), padx = 5,
                   bg = '#0F0F0F', fg = 'white', relief = 'groove',)
    lbl.place(x = 960, y = 20, anchor = 'n')
    
    root_inv = tk.Button(root, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'black', bg =  '#F1C40F', padx = 7)
    root_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    root_ext = tk.Button(root, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = '#F1C40F', fg = 'black', command = root.destroy)
    root_ext.place(x = 1916, y = 1076, anchor = 'se')

    root.mainloop()

story()
