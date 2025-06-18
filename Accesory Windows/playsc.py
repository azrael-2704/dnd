import tkinter as tk
from PIL import ImageTk, Image

def playsc_win():
    playsc = tk.Toplevel()
    playsc.attributes('-fullscreen', True)

    playsc_can=tk.Canvas(playsc, width=1920, height=1080, bg='black')
    playsc_can.pack(expand=True, fill='both')

    main_bg=ImageTk.PhotoImage(Image.open('D:\\Amartya\'s Files\\XII\\Computer Science\\Project\\Images\\Home Screen BG.jpg'))
    playsc_can.create_image(0, 0, image=main_bg, anchor='nw')

    playsc_new = tk.Button(playsc, text = 'New Game', padx = 30,
                           font = ('Enchanted Land', 90),
                           bg = '#272625', fg = 'white')
    playsc_new.place(x = 950, y = 430, anchor = 'e')

    playsc_lod = tk.Button(playsc, text = 'Load Game', padx = 30,
                           font = ('Enchanted Land', 90),
                           bg = '#272625', fg = 'white')
    playsc_lod.place(x = 970, y = 430, anchor = 'w')

    playsc_del = tk.Button(playsc, text = 'Delete Game', padx = 30,
                           font = ('Enchanted Land', 90),
                           bg = '#272625', fg = 'white')
    playsc_del.place(x = 960, y = 570, anchor = 'n')

    playsc_ext = tk.Button(playsc, text = 'Exit', font = ('Enchanted Land', 50), padx = 20,
                           bg = '#272625', fg = 'white', command = playsc.destroy)
    playsc_ext.place(x = 1900, y = 1060, anchor = 'se')

    playsc.mainloop()


playsc_win()
