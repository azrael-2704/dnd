import tkinter as tk
from PIL import ImageTk, Image

def homesc_win():
    sqlsc.after(500, lambda: sqlsc.destroy()) # REMOVE THIS LINE #
    homesc = tk.Tk() # CHANGE Tk TO Toplevel #
    homesc.title('Dungeons and Dragons')
    homesc.geometry('1920x1080')

    homesc_can=tk.Canvas(homesc, width=1920, height=1080, bg='black')
    homesc_can.pack(expand=True, fill='both')

    main_bg = ImageTk.PhotoImage(Image.open('Home Screen BG.jpg'))
    homesc_can.create_image(0, 0, image=main_bg, anchor='nw')

    homesc_head=tk.Label(homesc, text='Dungeons and Dragons',
               font=('Chiller', 100, 'bold'), bd=5,
               fg='white', bg='#0F0F0F', relief='ridge', padx=10, pady=2)
    homesc_head.place(x=960, y=10, anchor='n')

    homesc_subhead=tk.Label(homesc, text='A Game of Choices',
                   font=('Chiller', 60), bd=5,
                   fg='white', bg='#0F0F0F', relief='ridge', padx=10, pady=2)
    homesc_subhead.place(x=960, y=200, anchor='n')

    but_play=tk.Button(homesc, text='Play',
                       font=('Bahnschrift SemiBold SemiConden', 40),
                       bg='#272625', fg='white', padx=10, command=) ## ENTER THE PLAYSC FUNCTION ##
    but_play.place(x=960, y= 450, anchor='n')

    but_exit=tk.Button(homesc, text='Exit', padx=10,
                       font=('Bahnschrift SemiBold SemiConden', 40),
                       bg='#272625', fg='white', command=homesc.destroy)
    but_exit.place(x=960, y=600, anchor='n')

    homesc.mainloop()

homesc_win()
