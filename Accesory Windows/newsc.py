import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector as sql


con = sql.connect(host = 'localhost', user = 'root', passwd = 'lekedikhao')
if con.is_connected():
    print ('Connection Successful')
cur = con.cursor()


def get_svname():

    global save_name

    save_name = newsc_name.get()


def create_save():

    cur.execute('create database {};'.format(save_name))
    cur.execute('use {};'.format(save_name))
    cur.execute('create table Inventory(item_name varchar(50),quantity int(3),durability int(3));')
    cur.execute('create table Stats(health int(5), armour int(5));')
    cur.execute('create table Progress(story_part varchar(7));')


def newsc_win():

    global newsc, newsc_name

    #playsc.after(500, lambda: playsc.destroy())

    newsc = tk.Tk()
    newsc.title('Dungeons and Dragons')
    newsc.geometry('1920x1080')
    newsc.attributes('-fullscreen', True)

    newsc_can = tk.Canvas(newsc, width = 1920, height = 1080, bg = 'black')
    newsc_can.pack(expand = True, fill = 'both')

    main_bg = ImageTk.PhotoImage(Image.open('Home Screen BG.jpg'))
    newsc_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    newsc_head = tk.Label(newsc, text = 'Please Enter Player Name', padx = 10,
                          font = ('Enchanted Land', 70), pady = 5,
                          fg = 'white', bg = '#0F0F0F', relief = 'ridge', bd = 5)
    newsc_head.place(x = 570, y = 410, anchor = 's')

    newsc_name = tk.Entry(newsc, font = ('Enchanted Land', 70),
                          width = 20, bd = 7, relief = 'sunken', justify = 'center')
    newsc_name.place(x= 1225, y = 407, anchor = 's')

    newsc_sto = tk.Button(newsc, text = 'OK', bg = '#272625', fg = 'white', padx = 5,
                          font = ('Enchanted Land', 50), command = get_svname)
    newsc_sto.place(x = 1600, y = 410, anchor = 's')

    newsc_cre = tk.Button(newsc, text = 'Create Save', command = create_save,
                          font = ('Enchanted Land', 70),
                          bg = '#272625', fg = 'white', padx = 5)
    newsc_cre.place(x = 950, y = 600, anchor = 'e')

    newsc_proc = tk.Button(newsc, text = 'Proceed',
                           font = ('Enchanted Land', 70),
                           bg = '#272625', fg = 'white', padx = 5)
    newsc_proc.place(x = 970, y = 600, anchor = 'w')

    newsc_ext = tk.Button(newsc, text = 'Exit', font = ('Enchanted Land', 50), padx = 20,
                           bg = '#272625', fg = 'white', command = newsc.destroy)
    newsc_ext.place(x = 1900, y = 1060, anchor = 'se')

    newsc.mainloop()


newsc_win()
