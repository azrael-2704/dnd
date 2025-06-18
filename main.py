import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector as sql
from pygame import mixer
import os
import importlib.util
import sys

####################################################################################


# Pacakge Installer

def check_package(package_name):
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        print(f"{package_name} is NOT installed.")
        sys.exit(1)  # Exit if a package is missing
    else:
        print(f"{package_name} is installed.")

print("Checking required packages...")
check_package("tkinter")  # Built-in, should be available
check_package("PIL")  # Pillow (PIL) for image handling
check_package("mysql.connector")  # MySQL Connector
check_package("pygame")  # Pygame for audio handling
print("Package check completed.")


baseDir = os.getcwd()

ppath = 'Images\\'
kpath = 'Knight\\'
mpath = 'Monk\\'
tpath = 'Thief\\'
wpath = 'Wizard\\'


####################################################################################


# MySQL Connectivity Function #

def mysql_con():

    global con, cur, saves, main_bg, play_img, pause_img, health_icn, armour_icn

    try:
        con = sql.connect(host = 'localhost', user = 'root', passwd = sqlsc_txtb.get())
        if con.is_connected:
            confirm_lbl = tk.Label(sqlsc, text='Connection Successful', padx = 35,
                                   font=('Enchanted Land', 70), relief = 'groove',
                                   bg='black', fg='white', bd = 5)
            confirm_lbl.place(x = 960, y = 750, anchor = 'n')
            
            cur = con.cursor()

            saves = []

            cur.execute("show databases;")
            temp1 = cur.fetchall()
            for i in temp1:
                saves += i

            sqlsc_but.place(x = 1030, y = 600, anchor = 'e')
            sqlsc_prc.place(x = 1060, y = 600, anchor = 'w')

            main_bg = ImageTk.PhotoImage(Image.open('{}Home Screen BG.jpg'.format(ppath)))
            play_img = ImageTk.PhotoImage(Image.open('{}Music Play Icon.png'.format(ppath)))
            pause_img = ImageTk.PhotoImage(Image.open('{}Music Pause Icon.png'.format(ppath)))
            health_icn = ImageTk.PhotoImage(Image.open('{}Health Icon.png'.format(ppath)))
            armour_icn = ImageTk.PhotoImage(Image.open('{}Shield Icon.png'.format(ppath)))

    except sql.errors.ProgrammingError:
        unconfirm_lbl = tk.Label(sqlsc, text='Connection Unsuccessful', padx = 10,
                                   font=('Enchanted Land', 70), relief = 'groove',
                                   bg='black', fg='white', bd = 5)
        unconfirm_lbl.place(x = 960, y = 750, anchor = 'n')

    
# BACKGROUND  MUSIC #

mixer.init()
mixer.music.load("Main Track 1 Hour.mp3")
mixer.music.set_volume(0.04)


# Playing Audio Track #
def play_bgm():
    mixer.music.unpause()


# Pausing Audio Track #
def pause_bgm():
    mixer.music.pause()


# End Game #
def end_game():
    sqlsc.destroy()
    mixer.music.stop()


## MySQL SCREEN CONNECTOR WINDOW ##

def sqlsc_win():

    global sqlsc_txtb, sqlsc, sqlsc_prc, sqlsc_but

    mixer.music.play()

    sqlsc = tk.Tk()
    sqlsc.attributes('-fullscreen', True)

    sqlsc_can = tk.Canvas(sqlsc, width = 1920, height = 1080, bg='black')
    sqlsc_can.pack(expand = True, fill = 'both')

    main_bg = ImageTk.PhotoImage(Image.open('{}Home Screen BG.jpg'.format(ppath)))
    sqlsc_can.create_image(0, 0, image = main_bg, anchor = 'nw')
    
    sqlsc_head = tk.Label(sqlsc, text = 'MySQL Connectivity Gateway',
                          font = ('Enchanted Land', 100), bd = 5, relief = 'ridge',
                          bg = 'black', fg = 'white', padx = 10)
    sqlsc_head.place(x = 960, y = 20, anchor = 'n')

    sqlsc_lbl = tk.Label(sqlsc, text = 'Please Enter Your MySQL Password',
                         font = ('Enchanted Land', 50), bd = 5, relief  = 'ridge',
                         bg = 'black', fg = 'white', padx = 10)
    sqlsc_lbl.place(x = 950, y = 400, anchor = 'e')

    sqlsc_txtb = tk.Entry(sqlsc, show = '*', width = 35, relief = 'sunken',
                          justify = 'center',  bd = 5,
                          font = ('Enchanted Land', 50))
    sqlsc_txtb.place(x = 970, y = 400, anchor = 'w')

    sqlsc_but = tk.Button(sqlsc, text = 'Check Connection',
                          font = ('Enchanted Land', 50),
                          bg = '#272625', fg = 'white', command = mysql_con)
    sqlsc_but.place(x = 960, y = 600, anchor = 'center')

    sqlsc_prc = tk.Button(sqlsc, text = 'Proceed',
                          font = ('Enchanted Land', 50),
                          bg = '#272625', fg = 'white', command = homesc_win)

    play_img = ImageTk.PhotoImage(Image.open('{}Music Play Icon.png'.format(ppath)))
    sqlsc_pla = tk.Button(sqlsc, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    sqlsc_pla.place(x = 1865, y = 5, anchor = 'ne')

    pause_img = ImageTk.PhotoImage(Image.open('{}Music Pause Icon.png'.format(ppath)))
    sqlsc_pau = tk.Button(sqlsc, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    sqlsc_pau.place(x = 1915, y = 5, anchor = 'ne')

    sqlsc_ext = tk.Button(sqlsc, text = 'Exit', font = ('Enchanted Land', 50), padx = 20,
                           bg = '#272625', fg = 'white', command = end_game)
    sqlsc_ext.place(x = 1900, y = 1060, anchor = 'se')

    sqlsc.mainloop()


## HOME SCREEN WINDOW ##

def homesc_win():

    global homesc

    sqlsc.attributes('-fullscreen', False)
    sqlsc.geometry('1x10')

    homesc = tk.Toplevel()
    homesc.attributes('-fullscreen', True)

    homesc_can = tk.Canvas(homesc, width = 1920, height = 1080, bg='black')
    homesc_can.pack(expand = True, fill = 'both')

    homesc_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    homesc_head = tk.Label(homesc, text='Dungeons and Dragons', padx = 20,
                           font = ('Enchanted Land', 130, 'bold'), bd = 5,
                           fg = 'white', bg = '#0F0F0F', relief = 'ridge')
    homesc_head.place(x = 960, y = 10, anchor = 'n')

    homesc_subhead = tk.Label(homesc, text = 'A Game of Choices', padx = 20,
                              font = ('Enchanted Land', 90), bd = 5, fg = 'white',
                              bg = '#0F0F0F', relief = 'ridge')                              
    homesc_subhead.place(x = 960, y = 235, anchor = 'n')

    homesc_play = tk.Button(homesc, text = 'Play', padx = 10,
                            font = ('Enchanted Land', 70),
                            bg = '#272625', fg = 'white', command = playsc_win)
    homesc_play.place(x = 950, y = 640, anchor = 'e')

    homesc_pla = tk.Button(homesc, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    homesc_pla.place(x = 1865, y = 5, anchor = 'ne')

    homesc_pau = tk.Button(homesc, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    homesc_pau.place(x = 1915, y = 5, anchor = 'ne')

    homesc_exit=tk.Button(homesc, text = 'Exit', padx = 15,
                          font = ('Enchanted Land', 70),
                          bg = '#272625', fg = 'white', command = end_game)
    homesc_exit.place(x = 970, y = 640, anchor = 'w')

    homesc.mainloop()


## PLAY SCREEN WINDOW ##

def playsc_win():

    global playsc

    homesc.after(500, lambda: homesc.destroy())

    playsc = tk.Toplevel()
    playsc.attributes('-fullscreen', True)

    playsc_can = tk.Canvas(playsc, width = 1920, height = 1080, bg = 'black')
    playsc_can.pack(expand = True, fill = 'both')

    playsc_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    playsc_new = tk.Button(playsc, text = 'New Game', padx = 30,
                           font = ('Enchanted Land', 90),
                           bg = '#272625', fg = 'white', command = newsc_win)
    playsc_new.place(x = 950, y = 430, anchor = 'e')

    playsc_lod = tk.Button(playsc, text = 'Load Game', padx = 30,
                           font = ('Enchanted Land', 90),
                           bg = '#272625', fg = 'white', command=lodsc_win)
    playsc_lod.place(x = 970, y = 430, anchor = 'w')

    playsc_del = tk.Button(playsc, text = 'Delete Game', padx = 30,
                           font = ('Enchanted Land', 90),
                           bg = '#272625', fg = 'white', command = delsc_win)
    playsc_del.place(x = 960, y = 570, anchor = 'n')

    playsc_pla = tk.Button(playsc, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    playsc_pla.place(x = 1865, y = 5, anchor = 'ne')

    playsc_pau = tk.Button(playsc, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    playsc_pau.place(x = 1915, y = 5, anchor = 'ne')
    
    playsc_ext = tk.Button(playsc, text = 'Exit', font = ('Enchanted Land', 50), padx = 20,
                           bg = '#272625', fg = 'white', command = end_game)
    playsc_ext.place(x = 1900, y = 1060, anchor = 'se')

    playsc.mainloop()


# Create Save #

def create_save():

    global save_name

    save_name = newsc_name.get()

    cur.execute('show databases;')
    flag = False
    for  db in cur:
        if newsc_name.get().lower() in db:
            flag = True
            break
    if flag == False:
        cur.execute('create database {};'.format(save_name))
        cur.execute('use {};'.format(save_name))
        cur.execute('create table Inventory(item_name varchar(50),quantity int(10));')
        cur.execute('create table Stats(health int(5), armour int(5));')
        cur.execute('create table Progress(protagonist varchar(10), story_progress varchar(20));')

        sconf_lbl = tk.Label(newsc, text = 'Profile Created', font = ('Enchanted Land', 70),
                            bg = '#0F0F0F', fg = 'white', relief = 'ridge', bd = 5, padx = 5)
        sconf_lbl.place(x = 960, y = 750, anchor = 'n')

        saves.append(save_name)

        newsc_cre.place(x = 950, y = 600, anchor = 'e')
        newsc_proc.place(x = 970, y = 600, anchor = 'w')
    else:
        sconf_lbl = tk.Label(newsc, text = 'Profile Already Exists', font = ('Enchanted Land', 70),
                            bg = '#0F0F0F', fg = 'white', relief = 'ridge', bd = 5, padx = 5)
        sconf_lbl.place(x = 960, y = 750, anchor = 'n')
        
    
## NEW GAME SCREEN WINDOW ##

def newsc_win():

    global newsc, newsc_name, save_name, newsc_proc, newsc_cre

    newsc = tk.Toplevel()
    newsc.attributes('-fullscreen', True)

    newsc_can = tk.Canvas(newsc, width = 1920, height = 1080, bg = 'black')
    newsc_can.pack(expand = True, fill = 'both')

    newsc_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    newsc_head = tk.Label(newsc, text = 'Please Enter Player Name', padx = 10,
                          font = ('Enchanted Land', 70), pady = 5,
                          fg = 'white', bg = '#0F0F0F', relief = 'ridge', bd = 5)
    newsc_head.place(x = 570, y = 410, anchor = 's')

    newsc_name = tk.Entry(newsc, font = ('Enchanted Land', 70),
                          width = 25, bd = 7, relief = 'sunken', justify = 'center')
    newsc_name.place(x= 1325, y = 407, anchor = 's')

    newsc_cre = tk.Button(newsc, text = 'Create Save', command = create_save,
                          font = ('Enchanted Land', 70),
                          bg = '#272625', fg = 'white', padx = 5)
    newsc_cre.place(x = 960, y = 600, anchor = 'center')

    newsc_proc = tk.Button(newsc, text = 'Proceed', command = chrsc_win,
                           font = ('Enchanted Land', 70),
                           bg = '#272625', fg = 'white', padx = 40)

    newsc_pla = tk.Button(newsc, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    newsc_pla.place(x = 1865, y = 5, anchor = 'ne')

    newsc_pau = tk.Button(newsc, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    newsc_pau.place(x = 1915, y = 5, anchor = 'ne')

    newsc_ext = tk.Button(newsc, text = 'Back', font = ('Enchanted Land', 50), padx = 12,
                           bg = '#272625', fg = 'white', command = newsc.destroy)
    newsc_ext.place(x = 1900, y = 910, anchor = 'se')

    newsc_ext = tk.Button(newsc, text = 'Exit', font = ('Enchanted Land', 50), padx = 20,
                           bg = '#272625', fg = 'white', command = end_game)
    newsc_ext.place(x = 1900, y = 1060, anchor = 'se')

    newsc.mainloop()


## LOAD GAME SCREEN WINDOW ##

def lodsc_win():

    global lodsc, lodopt_name

    lodsc = tk.Toplevel()
    lodsc.attributes('-fullscreen', True)

    lodsc_can = tk.Canvas(lodsc, width = 1920, height = 1080, bg = 'black')
    lodsc_can.pack(expand = True, fill = 'both')

    lodsc_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    lodsc_head = tk.Label(lodsc, text = 'Please Enter Player Name', padx = 10,
                          font = ('Enchanted Land', 70), pady = 5,
                          fg = 'white', bg = '#0F0F0F', relief = 'ridge', bd = 5)
    lodsc_head.place(x = 570, y = 410, anchor = 's')

    lodopt_name = tk.StringVar()
    lodsc_name = tk.OptionMenu(lodsc, lodopt_name, *saves)
    lodsc_name.place(x= 1325, y = 407, anchor = 's')
    lodsc_name.config(bg = '#808080', width = 25)
    lodsc_name.config(font = ('Enchanted Land', 70))

    #lodsc_lod = tk.Button(lodsc, text = 'Load Game', command = loadgame,
                          #font = ('Enchanted Land', 70),
                          #bg = '#272625', fg = 'white', padx = 5)
    #lodsc_lod.place(x = 960, y = 600, anchor = 'center')
    
    lodsc_lod = tk.Button(lodsc, text = 'Load Game', command = loadgame,
                          font = ('Enchanted Land', 70),
                          bg = '#272625', fg = 'white', padx = 5)
    lodsc_lod.place(x = 950, y = 600, anchor = 'e')

    lodsc_gdm = tk.Button(lodsc, text = 'God Mode', command = godmodelog_win,
                          font = ('Enchanted Land', 70),
                          bg = '#272625', fg = 'white', padx = 5)
    lodsc_gdm.place(x = 970, y = 600, anchor = 'w')

    lodsc_pla = tk.Button(lodsc, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    lodsc_pla.place(x = 1865, y = 5, anchor = 'ne')

    lodsc_pau = tk.Button(lodsc, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    lodsc_pau.place(x = 1915, y = 5, anchor = 'ne')

    lodsc_bck = tk.Button(lodsc, text = 'Back', font = ('Enchanted Land', 50), padx = 12,
                           bg = '#272625', fg = 'white', command = lodsc.destroy)
    lodsc_bck.place(x = 1900, y = 910, anchor = 'se')

    lodsc_ext = tk.Button(lodsc, text = 'Exit', font = ('Enchanted Land', 50), padx = 20,
                           bg = '#272625', fg = 'white', command = end_game)
    lodsc_ext.place(x = 1900, y = 1060, anchor = 'se')

    lodsc.mainloop()


# Load Game #

def loadgame():

    load_name = lodopt_name.get()

    cur.execute('use {};'.format(load_name))
    cur.execute('select protagonist from progress;')
    temp1 = cur.fetchall()
    temp2 = temp1[0]

    if temp2[0] == 'knight':
        cur.execute('select story_progress from progress;')
        temp3 = cur.fetchall()
        temp4 = temp3[0]
        if temp4[0] == 'kntsc1':
            kntstr1()
        elif temp4[0] == 'kntsc2':
            kntstr2()
        elif temp4[0] == 'kntsc3':
            kntstr3()
        elif temp4[0] == 'kntsc4':
            kntstr4()
        elif temp4[0] == 'kntsc5':
            kntstr5()
        elif temp4[0] == 'kntsc6':
            kntstr6()
        elif temp4[0] == 'kntsc7':
            kntstr7()
        elif temp4[0] == 'kntsc8':
            kntstr8()
        elif temp4[0] == 'kntsc9':
            kntstr9()
        elif temp4[0] == 'kntsc10':
            kntstr10()
        elif temp4[0] == 'kntsc11':
            kntstr11()
        elif temp4[0] == 'kntsc12':
            kntstr12()
        elif temp4[0] == 'kntsc13':
            kntstr13()
        elif temp4[0] == 'kntsc14':
            kntstr14()
        elif temp4[0] == 'kntsc15':
            kntstr15()
        elif temp4[0] == 'kntsc16':
            kntstr16()
        elif temp4[0] == 'kntsc17':
            kntstr17()
        
    elif temp2[0] == 'monk':
        cur.execute('select story_progress from progress;')
        temp3 = cur.fetchall()
        temp4 = temp3[0]
        if temp4[0] == 'mnksc1':
            mnkstr1()
        elif temp4[0] == 'mnksc2':
            mnkstr2()
        elif temp4[0] == 'mnksc3':
            mnkstr3()
        elif temp4[0] == 'mnksc4':
            mnkstr4()
        elif temp4[0] == 'mnksc5':
            mnkstr5()
        elif temp4[0] == 'mnksc6':
            mnkstr6()
        elif temp4[0] == 'mnksc7':
            mnkstr7()
        elif temp4[0] == 'mnksc8':
            mnkstr8()
        elif temp4[0] == 'mnksc9':
            mnkstr9()
        elif temp4[0] == 'mnksc10':
            mnkstr10()
        elif temp4[0] == 'mnksc11':
            mnkstr11()
        elif temp4[0] == 'mnksc12':
            mnkstr12()
        elif temp4[0] == 'mnksc13':
            mnkstr13()
        elif temp4[0] == 'mnksc14':
            mnkstr14()
        elif temp4[0] == 'mnksc15':
            mnkstr15()
        elif temp4[0] == 'mnksc16':
            mnkstr16()
        elif temp4[0] == 'mnksc17':
            mnkstr17()
        
    elif temp2[0] == 'thief':
        cur.execute('select story_progress from progress;')
        temp3 = cur.fetchall()
        temp4 = temp3[0]
        if temp4[0] == 'thfsc1':
            thfstr1()
        elif temp4[0] == 'thfsc2':
            thfstr2()
        elif temp4[0] == 'thfsc3':
            thfstr3()
        elif temp4[0] == 'thfsc4':
            thfstr4()
        elif temp4[0] == 'thfsc5':
            thfstr5()
        elif temp4[0] == 'thfsc6':
            thfstr6()
        elif temp4[0] == 'thfsc7':
            thfstr7()
        elif temp4[0] == 'thfsc8':
            thfstr8()
        elif temp4[0] == 'thfsc9':
            thfstr9()
        elif temp4[0] == 'thfsc10':
            thfstr10()
        elif temp4[0] == 'thfsc11':
            thfstr11()
        elif temp4[0] == 'thfsc12':
            thfstr12()
        elif temp4[0] == 'thfsc13':
            thfstr13()
        elif temp4[0] == 'thfsc14':
            thfstr14()
        elif temp4[0] == 'thfsc15':
            thfstr15()
        elif temp4[0] == 'thfsc16':
            thfstr16()
        elif temp4[0] == 'thfsc17':
            thfstr17()
        
    elif temp2[0] == 'wizard':
        cur.execute('select story_progress from progress;')
        temp3 = cur.fetchall()
        temp4 = temp3[0]
        if temp4[0] == 'wizsc1':
            wizstr1()
        elif temp4[0] == 'wizsc2':
            wizstr2()
        elif temp4[0] == 'wizsc3':
            wizstr3()
        elif temp4[0] == 'wizsc4':
            wizstr4()
        elif temp4[0] == 'wizsc5':
            wizstr5()
        elif temp4[0] == 'wizsc6':
            wizstr6()
        elif temp4[0] == 'wizsc7':
            wizstr7()
        elif temp4[0] == 'wizsc8':
            wizstr8()
        elif temp4[0] == 'wizsc9':
            wizstr9()
        elif temp4[0] == 'wizsc10':
            wizstr10()
        elif temp4[0] == 'wizsc11':
            wizstr11()
        elif temp4[0] == 'wizsc12':
            wizstr12()
        elif temp4[0] == 'wizsc13':
            wizstr13()
        elif temp4[0] == 'wizsc14':
            wizstr14()
        elif temp4[0] == 'wizsc15':
            wizstr15()
        elif temp4[0] == 'wizsc16':
            wizstr16()
        elif temp4[0] == 'wizsc17':
            wizstr17()


# Get God Mode Password #

def get_pass():

    god_pswd = godmodelog_name.get()

    if god_pswd == 'ADmiN1243':
        god_lbl = tk.Label(godmodelog, text = 'Wrong Password', font = ('Enchanted Land', 70),
                            bg = '#0F0F0F', fg = 'white', relief = 'ridge', bd = 5, padx = 5)
        god_lbl.place(x = 960, y = 750, anchor = 'n')

        god_btn = tk.Button(godmodelog, font = (5), bd = 0, bg = '#12110F', command = godmode)
        god_btn.place(x = 10, y = 1070, anchor = 'sw')

    else:
        wrong_lbl = tk.Label(godmodelog, text = 'Wrong Password. Try Again!', font = ('Enchanted Land', 70),
                            bg = '#0F0F0F', fg = 'white', relief = 'ridge', bd = 5, padx = 5)
        wrong_lbl.place(x = 960, y = 750, anchor = 'n')


# GOD MODE LOGIN #

def godmodelog_win():

    global godmodelog, godmodelog_name

    godmodelog = tk.Toplevel()
    godmodelog.attributes('-fullscreen', True)

    godmodelog_can = tk.Canvas(godmodelog, width = 1920, height = 1080, bg = 'black')
    godmodelog_can.pack(expand = True, fill = 'both')

    godmodelog_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    godmodelog_head = tk.Label(godmodelog, text = 'Please Enter Password', padx = 10,
                          font = ('Enchanted Land', 70), pady = 5,
                          fg = 'white', bg = '#0F0F0F', relief = 'ridge', bd = 5)
    godmodelog_head.place(x = 570, y = 410, anchor = 's')

    godmodelog_name = tk.Entry(godmodelog, font = ('Enchanted Land', 70), show = '*',
                          width = 25, bd = 7, relief = 'sunken', justify = 'center')
    godmodelog_name.place(x= 1325, y = 407, anchor = 's')

    godmodelog_cre = tk.Button(godmodelog, text = 'Proceed', command = get_pass,
                          font = ('Enchanted Land', 70),
                          bg = '#272625', fg = 'white', padx = 5)
    godmodelog_cre.place(x = 960, y = 600, anchor = 'center')

    godmodelog_pla = tk.Button(godmodelog, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    godmodelog_pla.place(x = 1865, y = 5, anchor = 'ne')

    godmodelog_pau = tk.Button(godmodelog, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    godmodelog_pau.place(x = 1915, y = 5, anchor = 'ne')

    godmodelog_bck = tk.Button(godmodelog, text = 'Back', font = ('Enchanted Land', 50), padx = 12,
                           bg = '#272625', fg = 'white', command = godmodelog.destroy)
    godmodelog_bck.place(x = 1900, y = 910, anchor = 'se')

    godmodelog_ext = tk.Button(godmodelog, text = 'Exit', font = ('Enchanted Land', 50), padx = 20,
                           bg = '#272625', fg = 'white', command = end_game)
    godmodelog_ext.place(x = 1900, y = 1060, anchor = 'se')

    godmodelog.mainloop()


# GOD MODE #

def godmode():
    godmode = tk.Toplevel()
    godmode.attributes('-fullscreen', True)

    godmode_can = tk.Canvas(godmode, width = 1920, height = 1080, bg = 'black')
    godmode_can.pack(expand = True, fill = 'both')

    godmode_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    godmode.mainloop()


# Delete Save #

def del_save():

    del_name = delopt_name.get()
    
    cur.execute('drop database {};'.format(del_name))

    for i in saves:
        if i == del_name:
            saves.remove(del_name)

    dconf_lbl = tk.Label(delsc, text = 'Profile Deleted', font = ('Enchanted Land', 70),
                        bg = '#0F0F0F', fg = 'white', relief = 'ridge', bd = 5, padx = 5)
    dconf_lbl.place(x = 960, y = 750, anchor = 'n')


## DELETE GAME SCREEN WINDOW ##

def delsc_win():

    global delsc, delsc_name, delopt_name

    delsc = tk.Toplevel()
    delsc.attributes('-fullscreen', True)

    delsc_can = tk.Canvas(delsc, width = 1920, height = 1080, bg = 'black')
    delsc_can.pack(expand = True, fill = 'both')

    delsc_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    delsc_head = tk.Label(delsc, text = 'Please Enter Player Name', padx = 10,
                          font = ('Enchanted Land', 70), pady = 5,
                          fg = 'white', bg = '#0F0F0F', relief = 'ridge', bd = 5)
    delsc_head.place(x = 570, y = 410, anchor = 's')

    delopt_name = tk.StringVar()
    delsc_name = tk.OptionMenu(delsc, delopt_name, *saves)
    delsc_name.place(x= 1325, y = 407, anchor = 's')
    delsc_name.config(bg = '#808080', width = 25)
    delsc_name.config(font = ('Enchanted Land', 70))

    delsc_del = tk.Button(delsc, text = 'Delete Save', command = del_save,
                          font = ('Enchanted Land', 70),
                          bg = '#272625', fg = 'white', padx = 5)
    delsc_del.place(x = 960, y = 600, anchor = 'center')

    delsc_pla = tk.Button(delsc, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    delsc_pla.place(x = 1865, y = 5, anchor = 'ne')

    delsc_pau = tk.Button(delsc, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    delsc_pau.place(x = 1915, y = 5, anchor = 'ne')

    delsc_bck = tk.Button(delsc, text = 'Back', font = ('Enchanted Land', 50), padx = 12,
                           bg = '#272625', fg = 'white', command = delsc.destroy)
    delsc_bck.place(x = 1900, y = 910, anchor = 'se')

    delsc_ext = tk.Button(delsc, text = 'Exit', font = ('Enchanted Land', 50), padx = 20,
                           bg = '#272625', fg = 'white', command = end_game)
    delsc_ext.place(x = 1900, y = 1060, anchor = 'se')

    delsc.mainloop()


## CHARACTER SELECTION SCREEN WINDOW ##

def chrsc_win():

    global chrsc

    newsc.after(500, lambda: newsc.destroy())
    playsc.after(500, lambda: playsc.destroy())

    chrsc = tk.Toplevel()
    chrsc.attributes('-fullscreen', True)

    chrsc_can = tk.Canvas(chrsc, width = 1920, height = 1080, bg = 'black')
    chrsc_can.pack(expand = True, fill = 'both')

    chrsc_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    knt_bg = ImageTk.PhotoImage(Image.open('{}Knight.jpg'.format(kpath)))
    chrsc_knt = tk.Label(chrsc, padx = 0, pady = 0, relief = 'raised',
                         image = knt_bg, bd=5)
    chrsc_knt.place(x = 10, y = 10, anchor = 'nw')

    mnk_bg = ImageTk.PhotoImage(Image.open('{}Monk.jpg'.format(mpath)))
    chrsc_mnk = tk.Label(chrsc, padx = 0, pady = 0, relief = 'raised',
                         image = mnk_bg, bd=5)
    chrsc_mnk.place(x = 485, y = 10, anchor = 'nw')

    thf_bg = ImageTk.PhotoImage(Image.open('{}Thief.jpg'.format(tpath)))
    chrsc_thf = tk.Label(chrsc, padx = 0, pady = 0, relief = 'raised',
                         image = thf_bg, bd=5)
    chrsc_thf.place(x = 960, y = 10, anchor = 'nw')

    wiz_bg = ImageTk.PhotoImage(Image.open('{}Wizard.jpg'.format(wpath)))
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


#########################################################################################


# Knight Select #

def knt_opt():
    global opt
    opt = 'knight'
    cur.execute('insert into progress values ("{}", "kntsc1");'.format(opt))
    con.commit()
    kntstr1()


# Monk Select #

def mnk_opt():
    global opt
    opt = 'monk'
    cur.execute('insert into progress values ("{}", "mnksc1");'.format(opt))
    con.commit()
    mnkstr1()


# Thief Select #

def thf_opt():
    global opt
    opt = 'thief'
    cur.execute('insert into progress values ("{}", "thfsc1");'.format(opt))
    con.commit()
    thfstr1()

    
# Wizard Select #

def wiz_opt():
    global opt
    opt = 'wizard'
    cur.execute('insert into progress values ("{}", "wizsc1");'.format(opt))
    con.commit()
    wizstr1()
    

# Inventory Delete Options #

def del_item1():
    cur.execute('delete from inventory where item_name = "{}";'.format(item1_n))
    con.commit()
    invsc.destroy()
    inventory()
    
def del_item2():
    cur.execute('delete from inventory where item_name = "{}";'.format(item2_n))
    con.commit()
    invsc.destroy()
    inventory()

def del_item3():
    cur.execute('delete from inventory where item_name = "{}";'.format(item3_n))
    con.commit()
    invsc.destroy()
    inventory()

def del_item4():
    cur.execute('delete from inventory where item_name = "{}";'.format(item4_n))
    con.commit()
    invsc.destroy()
    inventory()

def del_item5():
    cur.execute('delete from inventory where item_name = "{}";'.format(item5_n))
    con.commit()
    invsc.destroy()
    inventory()

def del_item6():
    cur.execute('delete from inventory where item_name = "{}";'.format(item6_n))
    con.commit()
    invsc.destroy()
    inventory()

def del_item7():
    cur.execute('delete from inventory where item_name = "{}";'.format(item7_n))
    con.commit()
    invsc.destroy()
    inventory()

def del_item8():
    cur.execute('delete from inventory where item_name = "{}";'.format(item8_n))
    con.commit()
    invsc.destroy()
    inventory()

def del_item9():
    cur.execute('delete from inventory where item_name = "{}";'.format(item9_n))
    con.commit()
    invsc.destroy()
    inventory()

def del_item10():
    cur.execute('delete from inventory where item_name = "{}";'.format(item10_n))
    con.commit()
    invsc.destroy()
    inventory()


## INVENTORY ##

def inventory():

    global item1_n, item2_n, item3_n, item4_n, item5_n, item6_n, item7_n, item8_n, item9_n, item10_n

    cur.execute('select * from inventory;')
    temp = cur.fetchall()
    
    try:
        item1 = temp[0]
        item1_n = item1[0]
        item1_q = item1[1]
    except IndexError:
        pass

    try:
        item2 = temp[1]
        item2_n = item2[0]
        item2_q = item2[1]
    except IndexError:
        pass

    try:
        item3 = temp[2]
        item3_n = item3[0]
        item3_q = item3[1]
    except IndexError:
        pass

    try:
        item4 = temp[3]
        item4_n = item4[0]
        item4_q = item4[1]
    except IndexError:
        pass

    try:
        item5 = temp[4]
        item5_n = item5[0]
        item5_q = item5[1]
    except IndexError:
        pass

    try:
        item6 = temp[5]
        item6_n = item6[0]
        item6_q = item6[1]
    except IndexError:
        pass

    try:
        item7 = temp[6]
        item7_n = item7[0]
        item7_q = item7[1]
    except IndexError:
        pass

    try:
        item8 = temp[7]
        item8_n = item8[0]
        item8_q = item8[1]
    except IndexError:
        pass

    try:
        item9 = temp[8]
        item9_n = item9[0]
        item9_q = item9[1]
    except IndexError:
        pass

    try:
        item10 = temp[9]
        item10_n = item10[0]
        item10_q = item10[1]
    except IndexError:
        pass

    global invsc

    invsc = tk.Toplevel()
    invsc.geometry('1280x720')
    invsc.title('Inventory')
    
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

    try:
        invsc_l1 = tk.Label(invsc_fr1_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '{} {}'.format(item1_q, item1_n),
                            bg = '#342D25', fg = 'white')
        invsc_l1.pack(fill = 'both', expand = True)
    except UnboundLocalError:
        invsc_l1 = tk.Label(invsc_fr1_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '',
                            bg = '#342D25', fg = 'white')
        invsc_l1.pack(fill = 'both', expand = True)

    invsc_b1 = tk.Button(invsc_fr1, image = delete, bd = 0, command = del_item1)
    invsc_b1.pack(side = 'right')

    invsc_fr2 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr2.place(x = 100, y = 205, anchor = 'nw')
    invsc_fr2.propagate(0)

    invsc_fr2_1 = tk.Frame(invsc_fr2, width = 400, height = 100, bd = 0)
    invsc_fr2_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr2_1.propagate(0)

    try:
        invsc_l2 = tk.Label(invsc_fr2_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '{} {}'.format(item2_q, item2_n),
                            bg = '#342D25', fg = 'white')
        invsc_l2.pack(fill = 'both', expand = True)
    except UnboundLocalError:
        invsc_l2 = tk.Label(invsc_fr2_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '',
                            bg = '#342D25', fg = 'white')
        invsc_l2.pack(fill = 'both', expand = True)

    invsc_b2 = tk.Button(invsc_fr2, image = delete, bd = 0, command = del_item2)
    invsc_b2.pack(side = 'right')

    invsc_fr3 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr3.place(x = 100, y = 310, anchor = 'nw')
    invsc_fr3.propagate(0)

    invsc_fr3_1 = tk.Frame(invsc_fr3, width = 400, height = 100, bd = 0)
    invsc_fr3_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr3_1.propagate(0)

    try:
        invsc_l3 = tk.Label(invsc_fr3_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '{} {}'.format(item3_q, item3_n),
                            bg = '#342D25', fg = 'white')
        invsc_l3.pack(fill = 'both', expand = True)
    except UnboundLocalError:
        invsc_l3 = tk.Label(invsc_fr3_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '',
                            bg = '#342D25', fg = 'white')
        invsc_l3.pack(fill = 'both', expand = True)

    invsc_b3 = tk.Button(invsc_fr3, image = delete, bd = 0, command = del_item3)
    invsc_b3.pack(side = 'right')

    invsc_fr4 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr4.place(x = 100, y = 415, anchor = 'nw')
    invsc_fr4.propagate(0)

    invsc_fr4_1 = tk.Frame(invsc_fr4, width = 400, height = 100, bd = 0)
    invsc_fr4_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr4_1.propagate(0)

    try:
        invsc_l4 = tk.Label(invsc_fr4_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '{} {}'.format(item4_q, item4_n),
                            bg = '#342D25', fg = 'white')
        invsc_l4.pack(fill = 'both', expand = True)
    except UnboundLocalError:
        invsc_l4 = tk.Label(invsc_fr4_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '',
                            bg = '#342D25', fg = 'white')
        invsc_l4.pack(fill = 'both', expand = True)


    invsc_b4 = tk.Button(invsc_fr4, image = delete, bd = 0, command = del_item4)
    invsc_b4.pack(side = 'right')

    invsc_fr5 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr5.place(x = 100, y = 520, anchor = 'nw')
    invsc_fr5.propagate(0)

    invsc_fr5_1 = tk.Frame(invsc_fr5, width = 400, height = 100, bd = 0)
    invsc_fr5_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr5_1.propagate(0)

    try:
        invsc_l5 = tk.Label(invsc_fr5_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '{} {}'.format(item5_q, item5_n),
                            bg = '#342D25', fg = 'white')
        invsc_l5.pack(fill = 'both', expand = True)
    except UnboundLocalError:
        invsc_l5 = tk.Label(invsc_fr5_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '',
                            bg = '#342D25', fg = 'white')
        invsc_l5.pack(fill = 'both', expand = True)

    
    invsc_b5 = tk.Button(invsc_fr5, image = delete, bd = 0, command = del_item5)
    invsc_b5.pack(side = 'right')

    invsc_fr6 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr6.place(x = 1180, y = 100, anchor = 'ne')
    invsc_fr6.propagate(0)

    invsc_fr6_1 = tk.Frame(invsc_fr6, width = 400, height = 100, bd = 0)
    invsc_fr6_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr6_1.propagate(0)

    try:
        invsc_l6 = tk.Label(invsc_fr6_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '{} {}'.format(item6_q, item6_n),
                            bg = '#342D25', fg = 'white')
        invsc_l6.pack(fill = 'both', expand = True)
    except UnboundLocalError:
        invsc_l6 = tk.Label(invsc_fr6_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '',
                            bg = '#342D25', fg = 'white')
        invsc_l6.pack(fill = 'both', expand = True)


    invsc_b6 = tk.Button(invsc_fr6, image = delete, bd = 0, command = del_item6)
    invsc_b6.pack(side = 'right')

    invsc_fr7 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr7.place(x = 1180, y = 205, anchor = 'ne')
    invsc_fr7.propagate(0)

    invsc_fr7_1 = tk.Frame(invsc_fr7, width = 400, height = 100, bd = 0)
    invsc_fr7_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr7_1.propagate(0)

    try:
        invsc_l7 = tk.Label(invsc_fr7_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '{} {}'.format(item7_q, item7_n),
                            bg = '#342D25', fg = 'white')
        invsc_l7.pack(fill = 'both', expand = True)
    except UnboundLocalError:
        invsc_l7 = tk.Label(invsc_fr7_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '',
                            bg = '#342D25', fg = 'white')
        invsc_l7.pack(fill = 'both', expand = True)

    
    invsc_b7 = tk.Button(invsc_fr7, image = delete, bd = 0, command = del_item7)
    invsc_b7.pack(side = 'right')

    invsc_fr8 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr8.place(x = 1180, y = 310, anchor = 'ne')
    invsc_fr8.propagate(0)

    invsc_fr8_1 = tk.Frame(invsc_fr8, width = 400, height = 100, bd = 0)
    invsc_fr8_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr8_1.propagate(0)

    try:
        invsc_l8 = tk.Label(invsc_fr8_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '{} {}'.format(item8_q, item8_n),
                            bg = '#342D25', fg = 'white')
        invsc_l8.pack(fill = 'both', expand = True)
    except UnboundLocalError:
        invsc_l8 = tk.Label(invsc_fr8_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '',
                            bg = '#342D25', fg = 'white')
        invsc_l8.pack(fill = 'both', expand = True)
        

    invsc_b8 = tk.Button(invsc_fr8, image = delete, bd = 0, command = del_item8)
    invsc_b8.pack(side = 'right')

    invsc_fr9 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr9.place(x = 1180, y = 415, anchor = 'ne')
    invsc_fr9.propagate(0)

    invsc_fr9_1 = tk.Frame(invsc_fr9, width = 400, height = 100, bd = 0)
    invsc_fr9_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr9_1.propagate(0)

    try:
        invsc_l9 = tk.Label(invsc_fr9_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '{} {}'.format(item9_q, item9_n),
                            bg = '#342D25', fg = 'white')
        invsc_l9.pack(fill = 'both', expand = True)
    except UnboundLocalError:
        invsc_l9 = tk.Label(invsc_fr9_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '',
                            bg = '#342D25', fg = 'white')
        invsc_l9.pack(fill = 'both', expand = True)

    
    invsc_b9 = tk.Button(invsc_fr9, image = delete, bd = 0, command = del_item9)
    invsc_b9.pack(side = 'right')

    invsc_fr10 = tk.Frame(invsc, width = 500, height = 100)
    invsc_fr10.place(x = 1180, y = 520, anchor = 'ne')
    invsc_fr10.propagate(0)

    invsc_fr10_1 = tk.Frame(invsc_fr10, width = 400, height = 100, bd = 0)
    invsc_fr10_1.place(x = 0, y = 0, anchor = 'nw')
    invsc_fr10_1.propagate(0)

    try:
        invsc_l10 = tk.Label(invsc_fr10_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '{} {}'.format(item10_q, item10_n),
                            bg = '#342D25', fg = 'white')
        invsc_l10.pack(fill = 'both', expand = True)
    except UnboundLocalError:
        invsc_l10 = tk.Label(invsc_fr10_1, font = ('Enchanted Land', 50, 'bold'),
                            text = '',
                            bg = '#342D25', fg = 'white')
        invsc_l10.pack(fill = 'both', expand = True)

    invsc_b10 = tk.Button(invsc_fr10, image = delete, bd = 0, command = del_item10)
    invsc_b10.pack(side = 'right')
        
    invsc.mainloop()

    
#########################################################################################


## Knight's Story Begins ##

def kntstr1():
    
    global kntsc1

    try:
        chrsc.after(500, lambda: chrsc.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc1 = tk.Toplevel()
    kntsc1.attributes('-fullscreen', True)
    kntsc1.configure(bd = 0)

    kntsc1_can = tk.Canvas(kntsc1, width = 1920, height = 1080, bg = 'black')
    kntsc1_can.pack(expand = True, fill = 'both')
    
    kbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 1.jpg'.format(kpath)))
    kntsc1_can.create_image(0, 0, image = kbg1, anchor = 'nw')

    kntsc1_lbl = tk.Label(kntsc1, text = 'Welcome {}!'.format(save_name),
                   font = ('Enchanted Land', 100, 'bold'), padx = 20,
                   bg = '#0F0F0F', fg = 'white', relief = 'groove',)
    kntsc1_lbl.place(x = 960, y = 20, anchor = 'n')

    kntsc1_pla = tk.Button(kntsc1, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc1_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc1_pau = tk.Button(kntsc1, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc1_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc1_inv = tk.Button(kntsc1, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=kntstr2)
    kntsc1_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc1_ext = tk.Button(kntsc1, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    kntsc1_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc1";')
    con.commit()

    kntsc1.mainloop()

    
def kntstr2():
    
    global kntsc2

    try:
        kntsc1.after(500, lambda: kntsc1.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc2 = tk.Toplevel()
    kntsc2.attributes('-fullscreen', True)
    kntsc2.configure(bd = 0)

    kntsc2_can = tk.Canvas(kntsc2, width = 1920, height = 1080, bg = 'black')
    kntsc2_can.pack(expand = True, fill = 'both')
    
    kbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 2.jpg'.format(kpath)))
    kntsc2_can.create_image(0, 0, image = kbg1, anchor = 'nw')

    kntsc2_pla = tk.Button(kntsc2, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc2_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc2_pau = tk.Button(kntsc2, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc2_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc2_inv = tk.Button(kntsc2, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=kntstr3)
    kntsc2_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc2_ext = tk.Button(kntsc2, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    kntsc2_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc2";')
    con.commit()

    kntsc2.mainloop()


def kntstr3():
    
    global kntsc3

    try:
        kntsc2.after(500, lambda: kntsc2.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc3 = tk.Toplevel()
    kntsc3.attributes('-fullscreen', True)
    kntsc3.configure(bd = 0)

    kntsc3_can = tk.Canvas(kntsc3, width = 1920, height = 1080, bg = 'black')
    kntsc3_can.pack(expand = True, fill = 'both')
    
    kbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 3.jpg'.format(kpath)))
    kntsc3_can.create_image(0, 0, image = kbg1, anchor = 'nw')

    kntsc3_pla = tk.Button(kntsc3, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc3_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc3_pau = tk.Button(kntsc3, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc3_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc3_inv = tk.Button(kntsc3, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=kntstr4)
    kntsc3_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc3_ext = tk.Button(kntsc3, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    kntsc3_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc3";')
    con.commit()

    kntsc3.mainloop()


def kntstr4():
    
    global kntsc4

    try:
        kntsc3.after(500, lambda: kntsc3.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc4 = tk.Toplevel()
    kntsc4.attributes('-fullscreen', True)
    kntsc4.configure(bd = 0)

    kntsc4_can = tk.Canvas(kntsc4, width = 1920, height = 1080, bg = 'black')
    kntsc4_can.pack(expand = True, fill = 'both')
    
    kbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 4.jpg'.format(kpath)))
    kntsc4_can.create_image(0, 0, image = kbg1, anchor = 'nw')

    kntsc4_pla = tk.Button(kntsc4, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc4_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc4_pau = tk.Button(kntsc4, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc4_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc4_inv = tk.Button(kntsc4, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=kntstr5)
    kntsc4_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc4_ext = tk.Button(kntsc4, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    kntsc4_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc4";')
    con.commit()

    cur.execute('insert into stats values (100, 000);')
    con.commit()

    cur.execute('insert into inventory (item_name, quantity) values ("Knife", 1)')
    con.commit()

    cur.execute('insert into inventory (item_name, quantity) values ("Leftover Bread", 1)')
    con.commit()

    cur.execute('insert into inventory (item_name, quantity) values ("Gold Coins", 100)')
    con.commit()

    kntsc4.mainloop()



def kntstr5():
    
    global kntsc5

    try:
        kntsc4.after(500, lambda: kntsc4.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    cur.execute('select health from stats;')
    health1 = cur.fetchall()
    health2 = health1[0]

    cur.execute('select armour from stats;')
    armour1 = cur.fetchall()
    armour2 = armour1[0]

    kntsc5 = tk.Toplevel()
    kntsc5.attributes('-fullscreen', True)
    kntsc5.configure(bd = 1)

    kntsc5_can = tk.Canvas(kntsc5, width = 1920, height = 1080, bg = 'black')
    kntsc5_can.pack(expand = True, fill = 'both')
    
    kntsc5_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    kbg1 = ImageTk.PhotoImage(Image.open('{}Prot\'s House.jpg'.format(ppath)))
    kntsc5_pic1 = tk.Label(kntsc5, image = kbg1, bd=5)
    kntsc5_pic1.place(x = 0, y = 0, anchor = 'nw')

    kbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 1.jpg'.format(kpath)))
    kntsc5_pic2 = tk.Label(kntsc5, image = kbg2, bd=5)
    kntsc5_pic2.place(x = 1320, y = 0, anchor = 'nw')

    kntsc5_fr1 = tk.Frame(kntsc5, width = 555, height = 365, bg = 'red')
    kntsc5_fr1.place(x = 15, y = 700, anchor = 'nw')
    kntsc5_fr1.propagate(0)

    kntsc5_opt1 = tk.Button(kntsc5_fr1, text = 'Horse',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white',command=kntstr6)
    kntsc5_opt1.pack(fill = 'both', expand = True)

    kntsc5_fr2 = tk.Frame(kntsc5, width = 555, height = 365, bg = 'blue')
    kntsc5_fr2.place(x = 575, y = 700, anchor = 'nw')
    kntsc5_fr2.propagate(0)

    kntsc5_opt2 = tk.Button(kntsc5_fr2, text = 'On\nFoot',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white',command=kntstr7)
    kntsc5_opt2.pack(fill = 'both', expand = True)

    kntsc5_fr3 = tk.Frame(kntsc5, width = 550, height = 363, bg = 'green')
    kntsc5_fr3.place(x = 1135, y = 700, anchor = 'nw')
    kntsc5_fr3.propagate(0)

    kntsc5_opt3 = tk.Button(kntsc5_fr3, text = 'Use a Witch\'s\nTeleportation\nPotion',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white',command=kntstr8)
    kntsc5_opt3.pack(fill = 'both', expand = True)

    kntsc5_pla = tk.Button(kntsc5, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc5_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc5_pau = tk.Button(kntsc5, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc5_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc5_fr4 = tk.Frame(kntsc5, width = 125, height = 105, bg = 'red')
    kntsc5_fr4.place(x = 1790, y = 690, anchor = 'nw')
    kntsc5_fr4.propagate(0)

    kntsc5_heli = tk.Label(kntsc5, image = health_icn, bd = 0, bg = 'white')
    kntsc5_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    kntsc5_helt = tk.Label(kntsc5_fr4, text = health2[0], font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc5_helt.pack(fill = 'both', expand = True)

    kntsc5_fr5 = tk.Frame(kntsc5, width = 125, height = 105, bg = 'red')
    kntsc5_fr5.place(x = 1790, y = 790, anchor = 'nw')
    kntsc5_fr5.propagate(0)

    kntsc5_armi = tk.Label(kntsc5, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    kntsc5_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    kntsc5_armt = tk.Label(kntsc5_fr5, text = armour2[0], font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc5_armt.pack(fill = 'both', expand = True)

    kntsc5_inv = tk.Button(kntsc5, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    kntsc5_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc5_ext = tk.Button(kntsc5, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    kntsc5_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc5";')
    con.commit()

    kntsc5.mainloop()


def kntstr6():
    
    global kntsc6

    try:
        kntsc5.after(500, lambda: kntsc5.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc6 = tk.Toplevel()
    kntsc6.attributes('-fullscreen', True)
    kntsc6.configure(bd = 1)

    kntsc6_can = tk.Canvas(kntsc6, width = 1920, height = 1080, bg = 'black')
    kntsc6_can.pack(expand = True, fill = 'both')

    kntsc6_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    kbg1 = ImageTk.PhotoImage(Image.open('{}Ogre in a Jungle.jpg'.format(ppath)))
    kntsc6_pic1 = tk.Label(kntsc6, image = kbg1, bd=5)
    kntsc6_pic1.place(x = 0, y = 0, anchor = 'nw')

    kbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 2.jpg'.format(kpath)))
    kntsc6_pic2 = tk.Label(kntsc6, image = kbg2, bd=5)
    kntsc6_pic2.place(x = 1320, y = 0, anchor = 'nw')

    kntsc6_fr1 = tk.Frame(kntsc6, width = 555, height = 365, bg = 'red')
    kntsc6_fr1.place(x = 15, y = 700, anchor = 'nw')
    kntsc6_fr1.propagate(0)

    kntsc6_opt1 = tk.Button(kntsc6_fr1, font = ('Enchanted Land', 80),
                        text = 'signal your horse to leave',                            
                        bg = '#090D3A', fg = 'white', command = kntstr9)
    kntsc6_opt1.pack(fill = 'both', expand = True)

    kntsc6_fr2 = tk.Frame(kntsc6, width = 555, height = 365, bg = 'blue')
    kntsc6_fr2.place(x = 575, y = 700, anchor = 'nw')
    kntsc6_fr2.propagate(0)

    kntsc6_opt2 = tk.Button(kntsc6_fr2, font = ('Enchanted Land', 80),
                            text = 'Get off Your\n Horse Without Silently',                            
                            bg = '#090D3A', fg = 'white', command = kntstr10)
    kntsc6_opt2.pack(fill = 'both', expand = True)

    kntsc6_fr3 = tk.Frame(kntsc6, width = 550, height = 363, bg = 'green')
    kntsc6_fr3.place(x = 1135, y = 700, anchor = 'nw')
    kntsc6_fr3.propagate(0)

    kntsc6_opt3 = tk.Button(kntsc6_fr3, text = 'Attempt to Fight\n the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr11)
    kntsc6_opt3.pack(fill = 'both', expand = True)

    kntsc6_pla = tk.Button(kntsc6, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc6_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc6_pau = tk.Button(kntsc6, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc6_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc6_heli = tk.Label(kntsc6, image = health_icn, bd = 0, bg = 'white')
    kntsc6_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    kntsc6_helt = tk.Label(kntsc6, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc6_helt.place(x = 1916, y = 690, anchor = 'ne')

    kntsc6_armi = tk.Label(kntsc6, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    kntsc6_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    kntsc6_armt = tk.Label(kntsc6, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc6_armt.place(x = 1916, y = 790, anchor = 'ne')

    kntsc6_inv = tk.Button(kntsc6, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    kntsc6_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc6_ext = tk.Button(kntsc6, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    kntsc6_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc6";')
    con.commit()

    kntsc6.mainloop()



def kntstr7():
    
    global kntsc7

    try:
        kntsc5.after(500, lambda: kntsc5.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass
    
    kntsc7 = tk.Toplevel()
    kntsc7.attributes('-fullscreen', True)
    kntsc7.configure(bd = 1)

    kntsc7_can = tk.Canvas(kntsc7, width = 1920, height = 1080, bg = 'black')
    kntsc7_can.pack(expand = True, fill = 'both')

    kntsc7_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    kbg1 = ImageTk.PhotoImage(Image.open('{}Ogre in a Jungle.jpg'.format(ppath)))
    kntsc7_pic1 = tk.Label(kntsc7, image = kbg1, bd=5)
    kntsc7_pic1.place(x = 0, y = 0, anchor = 'nw')

    kbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 3.jpg'.format(kpath)))
    kntsc7_pic2 = tk.Label(kntsc7, image = kbg2, bd=5)
    kntsc7_pic2.place(x = 1320, y = 0, anchor = 'nw')

    kntsc7_fr1 = tk.Frame(kntsc7, width = 555, height = 365, bg = 'red')
    kntsc7_fr1.place(x = 15, y = 700, anchor = 'nw')
    kntsc7_fr1.propagate(0)

    kntsc7_opt1 = tk.Button(kntsc7_fr1, text = 'Attempt to\n Distract the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr12)
    kntsc7_opt1.pack(fill = 'both', expand = True)

    kntsc7_fr2 = tk.Frame(kntsc7, width = 555, height = 365, bg = 'blue')
    kntsc7_fr2.place(x = 575, y = 700, anchor = 'nw')
    kntsc7_fr2.propagate(0)

    kntsc7_opt2 = tk.Button(kntsc7_fr2, text = 'Attempt to\n Fight the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr11)
    kntsc7_opt2.pack(fill = 'both', expand = True)

    kntsc7_fr3 = tk.Frame(kntsc7, width = 550, height = 363, bg = 'green')
    kntsc7_fr3.place(x = 1135, y = 700, anchor = 'nw')
    kntsc7_fr3.propagate(0)

    kntsc7_opt3 = tk.Button(kntsc7_fr3, text = 'Hide and Hope\n that the Ogre\n Goes Away',
                        font = ('Enchanted Land', 80),
                        bg = '#090D3A', fg = 'white', command = kntstr13)
    kntsc7_opt3.pack(fill = 'both', expand = True)

    kntsc7_pla = tk.Button(kntsc7, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc7_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc7_pau = tk.Button(kntsc7, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc7_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc7_heli = tk.Label(kntsc7, image = health_icn, bd = 0, bg = 'white')
    kntsc7_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    kntsc7_helt = tk.Label(kntsc7, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc7_helt.place(x = 1916, y = 690, anchor = 'ne')

    kntsc7_armi = tk.Label(kntsc7, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    kntsc7_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    kntsc7_armt = tk.Label(kntsc7, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc7_armt.place(x = 1916, y = 790, anchor = 'ne')

    kntsc7_inv = tk.Button(kntsc7, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    kntsc7_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc7_ext = tk.Button(kntsc7, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    kntsc7_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc7";')
    con.commit()

    kntsc7.mainloop()



def kntstr8():
    
    global kntsc8

    try:
        kntsc5.after(500, lambda: kntsc5.destroy())
    except NameError:
        pass

    try:
        kntsc11.after(500, lambda: kntsc11.destroy())
    except NameError:
        pass

    try:
        kntsc12.after(500, lambda: kntsc12.destroy())
    except NameError:
        pass

    try:
        kntsc13.after(500, lambda: kntsc13.destroy())
    except NameError:
        pass

    try:
        kntsc14.after(500, lambda: kntsc14.destroy())
    except NameError:
        pass

    try:
        kntsc15.after(500, lambda: kntsc15.destroy())
    except NameError:
        pass

    try:
        kntsc17.after(500, lambda: kntsc17.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc8 = tk.Toplevel()
    kntsc8.attributes('-fullscreen', True)
    kntsc8.configure(bd = 0)

    kntsc8_can = tk.Canvas(kntsc8, width = 1920, height = 1080, bg = 'black')
    kntsc8_can.pack(expand = True, fill = 'both')
    
    kbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 5.jpg'.format(kpath)))
    kntsc8_can.create_image(0, 0, image = kbg1, anchor = 'nw')

    kntsc8_pla = tk.Button(kntsc8, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc8_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc8_pau = tk.Button(kntsc8, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc8_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc8_ext = tk.Button(kntsc8, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    kntsc8_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc8";')
    con.commit()

    kntsc8.mainloop()



def kntstr9():
    
    global kntsc9

    try:
        kntsc6.after(500, lambda: kntsc6.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc9 = tk.Toplevel()
    kntsc9.attributes('-fullscreen', True)
    kntsc9.configure(bd = 1)

    kntsc9_can = tk.Canvas(kntsc9, width = 1920, height = 1080, bg = 'black')
    kntsc9_can.pack(expand = True, fill = 'both')

    kntsc9_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    kbg1 = ImageTk.PhotoImage(Image.open('{}Horsecart 1.jpg'.format(ppath)))
    kntsc9_pic1 = tk.Label(kntsc9, image = kbg1, bd=5)
    kntsc9_pic1.place(x = 0, y = 0, anchor = 'nw')

    kbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 4.jpg'.format(kpath)))
    kntsc9_pic2 = tk.Label(kntsc9, image = kbg2, bd=5)
    kntsc9_pic2.place(x = 1320, y = 0, anchor = 'nw')

    kntsc9_fr1 = tk.Frame(kntsc9, width = 555, height = 365, bg = 'red')
    kntsc9_fr1.place(x = 15, y = 700, anchor = 'nw')
    kntsc9_fr1.propagate(0)

    kntsc9_opt1 = tk.Button(kntsc9_fr1, text = 'Attempt to\n Distract the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr12)
    kntsc9_opt1.pack(fill = 'both', expand = True)

    kntsc9_fr2 = tk.Frame(kntsc9, width = 555, height = 365, bg = 'blue')
    kntsc9_fr2.place(x = 575, y = 700, anchor = 'nw')
    kntsc9_fr2.propagate(0)

    kntsc9_opt2 = tk.Button(kntsc9_fr2, text = 'Attempt to\n Fight the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr11)
    kntsc9_opt2.pack(fill = 'both', expand = True)

    kntsc9_fr3 = tk.Frame(kntsc9, width = 550, height = 363, bg = 'green')
    kntsc9_fr3.place(x = 1135, y = 700, anchor = 'nw')
    kntsc9_fr3.propagate(0)

    kntsc9_opt3 = tk.Button(kntsc9_fr3, text = 'Hide and Hope\nthat the Ogre\nGoes Away',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr13)
    kntsc9_opt3.pack(fill = 'both', expand = True)

    kntsc9_pla = tk.Button(kntsc9, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc9_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc9_pau = tk.Button(kntsc9, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc9_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc9_heli = tk.Label(kntsc9, image = health_icn, bd = 0, bg = 'white')
    kntsc9_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    kntsc9_helt = tk.Label(kntsc9, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc9_helt.place(x = 1916, y = 690, anchor = 'ne')

    kntsc9_armi = tk.Label(kntsc9, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    kntsc9_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    kntsc9_armt = tk.Label(kntsc9, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc9_armt.place(x = 1916, y = 790, anchor = 'ne')

    kntsc9_inv = tk.Button(kntsc9, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    kntsc9_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc9_ext = tk.Button(kntsc9, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    kntsc9_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc9";')
    con.commit()

    kntsc9.mainloop()



def kntstr10():
    
    global kntsc10

    try:
        kntsc6.after(500, lambda: kntsc6.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc10 = tk.Toplevel()
    kntsc10.attributes('-fullscreen', True)
    kntsc10.configure(bd = 1)

    kntsc10_can = tk.Canvas(kntsc10, width = 1920, height = 1080, bg = 'black')
    kntsc10_can.pack(expand = True, fill = 'both')

    kntsc10_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    kbg1 = ImageTk.PhotoImage(Image.open('{}Wagon.jpg'.format(ppath)))
    kntsc10_pic1 = tk.Label(kntsc10, image = kbg1, bd=5)
    kntsc10_pic1.place(x = 0, y = 0, anchor = 'nw')

    kbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 5.jpg'.format(kpath)))
    kntsc10_pic2 = tk.Label(kntsc10, image = kbg2, bd=5)
    kntsc10_pic2.place(x = 1320, y = 0, anchor = 'nw')

    kntsc10_fr1 = tk.Frame(kntsc10, width = 555, height = 365, bg = 'red')
    kntsc10_fr1.place(x = 15, y = 700, anchor = 'nw')
    kntsc10_fr1.propagate(0)

    kntsc10_opt1 = tk.Button(kntsc10_fr1, text = 'Attempt to\n Distract the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr12)
    kntsc10_opt1.pack(fill = 'both', expand = True)

    kntsc10_fr2 = tk.Frame(kntsc10, width = 555, height = 365, bg = 'blue')
    kntsc10_fr2.place(x = 575, y = 700, anchor = 'nw')
    kntsc10_fr2.propagate(0)

    kntsc10_opt2 = tk.Button(kntsc10_fr2, text = 'Attempt to\n Fight the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr11)
    kntsc10_opt2.pack(fill = 'both', expand = True)

    kntsc10_fr3 = tk.Frame(kntsc10, width = 550, height = 363, bg = 'green')
    kntsc10_fr3.place(x = 1135, y = 700, anchor = 'nw')
    kntsc10_fr3.propagate(0)

    kntsc10_opt3 = tk.Button(kntsc10_fr3, text = 'Hide and Hope\n that the Ogre\n Goes Away',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr13)
    kntsc10_opt3.pack(fill = 'both', expand = True)

    kntsc10_pla = tk.Button(kntsc10, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc10_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc10_pau = tk.Button(kntsc10, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc10_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc10_heli = tk.Label(kntsc10, image = health_icn, bd = 0, bg = 'white')
    kntsc10_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    kntsc10_helt = tk.Label(kntsc10, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc10_helt.place(x = 1916, y = 690, anchor = 'ne')

    kntsc10_armi = tk.Label(kntsc10, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    kntsc10_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    kntsc10_armt = tk.Label(kntsc10, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc10_armt.place(x = 1916, y = 790, anchor = 'ne')

    kntsc10_inv = tk.Button(kntsc10, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    kntsc10_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc10_ext = tk.Button(kntsc10, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    kntsc10_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc10";')
    con.commit()

    kntsc10.mainloop()



def kntstr11():
    
    global kntsc11

    try:
        kntsc6.after(500, lambda: kntsc6.destroy())
    except NameError:
        pass

    try:
        kntsc7.after(500, lambda: kntsc7.destroy())
    except NameError:
        pass

    try:
        kntsc9.after(500, lambda: kntsc9.destroy())
    except NameError:
        pass

    try:
        kntsc10.after(500, lambda: kntsc10.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc11 = tk.Toplevel()
    kntsc11.attributes('-fullscreen', True)
    kntsc11.configure(bd = 1)

    kntsc11_can = tk.Canvas(kntsc11, width = 1920, height = 1080, bg = 'black')
    kntsc11_can.pack(expand = True, fill = 'both')

    kntsc11_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    kbg1 = ImageTk.PhotoImage(Image.open('{}Ogre Fight.jpg'.format(ppath)))
    kntsc11_pic1 = tk.Label(kntsc11, image = kbg1, bd=5)
    kntsc11_pic1.place(x = 0, y = 0, anchor = 'nw')

    kbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 6.jpg'.format(kpath)))
    kntsc11_pic2 = tk.Label(kntsc11, image = kbg2, bd=5)
    kntsc11_pic2.place(x = 1320, y = 0, anchor = 'nw')

    kntsc11_fr1 = tk.Frame(kntsc11, width = 555, height = 365, bg = 'red')
    kntsc11_fr1.place(x = 15, y = 700, anchor = 'nw')
    kntsc11_fr1.propagate(0)

    kntsc11_opt1 = tk.Button(kntsc11_fr1, text = 'Poison\nthe Ogre using a\nPoisoned Blade',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = kntstr14)
    kntsc11_opt1.pack(fill = 'both', expand = True)

    kntsc11_fr2 = tk.Frame(kntsc11, width = 555, height = 365, bg = 'blue')
    kntsc11_fr2.place(x = 575, y = 700, anchor = 'nw')
    kntsc11_fr2.propagate(0)

    kntsc11_opt2 = tk.Button(kntsc11_fr2, text = 'Paralyze\nthe Ogre\nUsing Chains',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = kntstr15)
    kntsc11_opt2.pack(fill = 'both', expand = True)

    kntsc11_fr3 = tk.Frame(kntsc11, width = 550, height = 363, bg = 'green')
    kntsc11_fr3.place(x = 1135, y = 700, anchor = 'nw')
    kntsc11_fr3.propagate(0)

    kntsc11_opt3 = tk.Button(kntsc11_fr3, text = 'Use Your Knife\n to Attack',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr8)
    kntsc11_opt3.pack(fill = 'both', expand = True)

    kntsc11_pla = tk.Button(kntsc11, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc11_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc11_pau = tk.Button(kntsc11, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc11_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc11_heli = tk.Label(kntsc11, image = health_icn, bd = 0, bg = 'white')
    kntsc11_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    kntsc11_helt = tk.Label(kntsc11, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc11_helt.place(x = 1916, y = 690, anchor = 'ne')

    kntsc11_armi = tk.Label(kntsc11, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    kntsc11_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    kntsc11_armt = tk.Label(kntsc11, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc11_armt.place(x = 1916, y = 790, anchor = 'ne')

    kntsc11_inv = tk.Button(kntsc11, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    kntsc11_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc11_ext = tk.Button(kntsc11, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    kntsc11_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc11";')
    con.commit()

    kntsc11.mainloop()



def kntstr12():
    
    global kntsc12

    try:
        kntsc7.after(500, lambda: kntsc7.destroy())
    except NameError:
        pass

    try:
        kntsc9.after(500, lambda: kntsc9.destroy())
    except NameError:
        pass

    try:
        kntsc10.after(500, lambda: kntsc10.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc12 = tk.Toplevel()
    kntsc12.attributes('-fullscreen', True)
    kntsc12.configure(bd = 1)

    kntsc12_can = tk.Canvas(kntsc12, width = 1920, height = 1080, bg = 'black')
    kntsc12_can.pack(expand = True, fill = 'both')

    kntsc12_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    kbg1 = ImageTk.PhotoImage(Image.open('{}Wizard Story.jpg'.format(ppath)))
    kntsc12_pic1 = tk.Label(kntsc12, image = kbg1, bd=5)
    kntsc12_pic1.place(x = 0, y = 0, anchor = 'nw')

    kbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 7.jpg'.format(kpath)))
    kntsc12_pic2 = tk.Label(kntsc12, image = kbg2, bd=5)
    kntsc12_pic2.place(x = 1320, y = 0, anchor = 'nw')

    kntsc12_fr1 = tk.Frame(kntsc12, width = 555, height = 365, bg = 'red')
    kntsc12_fr1.place(x = 15, y = 700, anchor = 'nw')
    kntsc12_fr1.propagate(0)

    kntsc12_opt1 = tk.Button(kntsc12_fr1, font = ('Enchanted Land', 55),
                             text = 'Slash a Tree With\nYour Broadsword\n and Run ',
                             bg = '#090D3A', fg = 'white', command = kntstr16)
    kntsc12_opt1.pack(fill = 'both', expand = True)

    kntsc12_fr2 = tk.Frame(kntsc12, width = 555, height = 365, bg = 'blue')
    kntsc12_fr2.place(x = 575, y = 700, anchor = 'nw')
    kntsc12_fr2.propagate(0)

    kntsc12_opt2 = tk.Button(kntsc12_fr2, text = 'Use a Smokebomb',
                            font = ('Enchanted Land', 70),
                            bg = '#090D3A', fg = 'white', command = kntstr17)
    kntsc12_opt2.pack(fill = 'both', expand = True)

    kntsc12_fr3 = tk.Frame(kntsc12, width = 550, height = 363, bg = 'green')
    kntsc12_fr3.place(x = 1135, y = 700, anchor = 'nw')
    kntsc12_fr3.propagate(0)

    kntsc12_opt3 = tk.Button(kntsc12_fr3, text = 'Throw a Big Rock\n in the Lake Nearby',
                            font = ('Enchanted Land', 75),
                            bg = '#090D3A', fg = 'white', command = kntstr8)
    kntsc12_opt3.pack(fill = 'both', expand = True)

    kntsc12_pla = tk.Button(kntsc12, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc12_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc12_pau = tk.Button(kntsc12, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc12_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc12_heli = tk.Label(kntsc12, image = health_icn, bd = 0, bg = 'white')
    kntsc12_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    kntsc12_helt = tk.Label(kntsc12, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc12_helt.place(x = 1916, y = 690, anchor = 'ne')

    kntsc12_armi = tk.Label(kntsc12, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    kntsc12_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    kntsc12_armt = tk.Label(kntsc12, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc12_armt.place(x = 1916, y = 790, anchor = 'ne')

    kntsc12_inv = tk.Button(kntsc12, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    kntsc12_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc12_ext = tk.Button(kntsc12, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    kntsc12_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc12";')
    con.commit()

    kntsc12.mainloop()




def kntstr13():
    
    global kntsc13

    try:
        kntsc7.after(500, lambda: kntsc7.destroy())
    except NameError:
        pass

    try:
        kntsc9.after(500, lambda: kntsc9.destroy())
    except NameError:
        pass

    try:
        kntsc10.after(500, lambda: kntsc10.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc13 = tk.Toplevel()
    kntsc13.attributes('-fullscreen', True)
    kntsc13.configure(bd = 1)

    kntsc13_can = tk.Canvas(kntsc13, width = 1920, height = 1080, bg = 'black')
    kntsc13_can.pack(expand = True, fill = 'both')

    kntsc13_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    kbg1 = ImageTk.PhotoImage(Image.open('{}Ogre Fight.jpg'.format(ppath)))
    kntsc13_pic1 = tk.Label(kntsc13, image = kbg1, bd=5)
    kntsc13_pic1.place(x = 0, y = 0, anchor = 'nw')

    kbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 8.jpg'.format(kpath)))
    kntsc13_pic2 = tk.Label(kntsc13, image = kbg2, bd=5)
    kntsc13_pic2.place(x = 1320, y = 0, anchor = 'nw')

    kntsc13_fr1 = tk.Frame(kntsc13, width = 555, height = 365, bg = 'red')
    kntsc13_fr1.place(x = 15, y = 700, anchor = 'nw')
    kntsc13_fr1.propagate(0)

    kntsc13_opt1 = tk.Button(kntsc13_fr1, text = 'Poison\nthe Ogre Using a\nPoisoned Blade',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = kntstr14)
    kntsc13_opt1.pack(fill = 'both', expand = True)

    kntsc13_fr2 = tk.Frame(kntsc13, width = 555, height = 365, bg = 'blue')
    kntsc13_fr2.place(x = 575, y = 700, anchor = 'nw')
    kntsc13_fr2.propagate(0)

    kntsc13_opt2 = tk.Button(kntsc13_fr2, text = 'Paralyze\nthe Ogre\nUsing Chains',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = kntstr15)
    kntsc13_opt2.pack(fill = 'both', expand = True)

    kntsc13_fr3 = tk.Frame(kntsc13, width = 550, height = 363, bg = 'green')
    kntsc13_fr3.place(x = 1135, y = 700, anchor = 'nw')
    kntsc13_fr3.propagate(0)

    kntsc13_opt3 = tk.Button(kntsc13_fr3, text = 'Try to Stab\n the Ogre with\n Your Knife',
                            font = ('Enchanted Land', 70),
                            bg = '#090D3A', fg = 'white', command = kntstr8)
    kntsc13_opt3.pack(fill = 'both', expand = True)

    kntsc13_pla = tk.Button(kntsc13, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc13_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc13_pau = tk.Button(kntsc13, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc13_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc13_heli = tk.Label(kntsc13, image = health_icn, bd = 0, bg = 'white')
    kntsc13_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    kntsc13_helt = tk.Label(kntsc13, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc13_helt.place(x = 1916, y = 690, anchor = 'ne')

    kntsc13_armi = tk.Label(kntsc13, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    kntsc13_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    kntsc13_armt = tk.Label(kntsc13, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc13_armt.place(x = 1916, y = 790, anchor = 'ne')

    kntsc13_inv = tk.Button(kntsc13, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    kntsc13_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc13_ext = tk.Button(kntsc13, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    kntsc13_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc13";')
    con.commit()

    kntsc13.mainloop()



def kntstr14():
    
    global kntsc14

    try:
        kntsc11.after(500, lambda: kntsc11.destroy())
    except NameError:
        pass

    try:
        kntsc13.after(500, lambda: kntsc13.destroy())
    except NameError:
        pass

    try:
        kntsc17.after(500, lambda: kntsc17.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc14 = tk.Toplevel()
    kntsc14.attributes('-fullscreen', True)
    kntsc14.configure(bd = 1)

    kntsc14_can = tk.Canvas(kntsc14, width = 1920, height = 1080, bg = 'black')
    kntsc14_can.pack(expand = True, fill = 'both')
    
    kntsc14_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    kbg1 = ImageTk.PhotoImage(Image.open('{}Poison.jpg'.format(ppath)))
    kntsc14_pic1 = tk.Label(kntsc14, image = kbg1, bd=5)
    kntsc14_pic1.place(x = 0, y = 0, anchor = 'nw')

    kbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 9.jpg'.format(kpath)))
    kntsc14_pic2 = tk.Label(kntsc14, image = kbg2, bd=5)
    kntsc14_pic2.place(x = 1320, y = 0, anchor = 'nw')

    kntsc14_fr1 = tk.Frame(kntsc14, width = 555, height = 365, bg = 'red')
    kntsc14_fr1.place(x = 15, y = 700, anchor = 'nw')
    kntsc14_fr1.propagate(0)

    kntsc14_opt1 = tk.Button(kntsc14_fr1, text = 'Knock it\nUnconcious\n with your Sword\'s Hilt',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr16)
    kntsc14_opt1.pack(fill = 'both', expand = True)

    kntsc14_fr2 = tk.Frame(kntsc14, width = 555, height = 365, bg = 'blue')
    kntsc14_fr2.place(x = 575, y = 700, anchor = 'nw')
    kntsc14_fr2.propagate(0)

    kntsc14_opt2 = tk.Button(kntsc14_fr2, text = 'Use Your Knife to\nPut an End to\n the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr16)
    kntsc14_opt2.pack(fill = 'both', expand = True)

    kntsc14_fr3 = tk.Frame(kntsc14, width = 550, height = 363, bg = 'green')
    kntsc14_fr3.place(x = 1135, y = 700, anchor = 'nw')
    kntsc14_fr3.propagate(0)

    kntsc14_opt3 = tk.Button(kntsc14_fr3, text = 'Leave the Ogre\n and Let Time Put\n an End to it',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr8)
    kntsc14_opt3.pack(fill = 'both', expand = True)

    kntsc14_pla = tk.Button(kntsc14, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc14_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc14_pau = tk.Button(kntsc14, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc14_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc14_heli = tk.Label(kntsc14, image = health_icn, bd = 0, bg = 'white')
    kntsc14_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    kntsc14_helt = tk.Label(kntsc14, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc14_helt.place(x = 1916, y = 690, anchor = 'ne')

    kntsc14_armi = tk.Label(kntsc14, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    kntsc14_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    kntsc14_armt = tk.Label(kntsc14, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc14_armt.place(x = 1916, y = 790, anchor = 'ne')

    kntsc14_inv = tk.Button(kntsc14, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    kntsc14_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc14_ext = tk.Button(kntsc14, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    kntsc14_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc14";')
    con.commit()

    kntsc14.mainloop()



def kntstr15():
    
    global kntsc15

    try:
        kntsc11.after(500, lambda: kntsc11.destroy())
    except NameError:
        pass

    try:
        kntsc13.after(500, lambda: kntsc13.destroy())
    except NameError:
        pass

    try:
        kntsc17.after(500, lambda: kntsc17.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc15 = tk.Toplevel()
    kntsc15.attributes('-fullscreen', True)
    kntsc15.configure(bd = 1)

    kntsc15_can = tk.Canvas(kntsc15, width = 1920, height = 1080, bg = 'black')
    kntsc15_can.pack(expand = True, fill = 'both')
    
    kntsc15_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    kbg1 = ImageTk.PhotoImage(Image.open('{}Chains.jpg'.format(ppath)))
    kntsc15_pic1 = tk.Label(kntsc15, image = kbg1, bd=5)
    kntsc15_pic1.place(x = 0, y = 0, anchor = 'nw')

    kbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 10.jpg'.format(kpath)))
    kntsc15_pic2 = tk.Label(kntsc15, image = kbg2, bd=5)
    kntsc15_pic2.place(x = 1320, y = 0, anchor = 'nw')

    kntsc15_fr1 = tk.Frame(kntsc15, width = 555, height = 365, bg = 'red')
    kntsc15_fr1.place(x = 15, y = 700, anchor = 'nw')
    kntsc15_fr1.propagate(0)

    kntsc15_opt1 = tk.Button(kntsc15_fr1, text = 'Knock it\nUnconcious\n with your Sword\'s Hilt',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr16)
    kntsc15_opt1.pack(fill = 'both', expand = True)

    kntsc15_fr2 = tk.Frame(kntsc15, width = 555, height = 365, bg = 'blue')
    kntsc15_fr2.place(x = 575, y = 700, anchor = 'nw')
    kntsc15_fr2.propagate(0)

    kntsc15_opt2 = tk.Button(kntsc15_fr2, text = 'Use Your Knife\nto Put an End\nto the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr16)
    kntsc15_opt2.pack(fill = 'both', expand = True)

    kntsc15_fr3 = tk.Frame(kntsc15, width = 550, height = 363, bg = 'green')
    kntsc15_fr3.place(x = 1135, y = 700, anchor = 'nw')
    kntsc15_fr3.propagate(0)

    kntsc15_opt3 = tk.Button(kntsc15_fr3, text = 'Make a\nRun for it',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = kntstr8)
    kntsc15_opt3.pack(fill = 'both', expand = True)

    kntsc15_pla = tk.Button(kntsc15, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc15_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc15_pau = tk.Button(kntsc15, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc15_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc15_heli = tk.Label(kntsc15, image = health_icn, bd = 0, bg = 'white')
    kntsc15_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    kntsc15_helt = tk.Label(kntsc15, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc15_helt.place(x = 1916, y = 690, anchor = 'ne')

    kntsc15_armi = tk.Label(kntsc15, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    kntsc15_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    kntsc15_armt = tk.Label(kntsc15, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc15_armt.place(x = 1916, y = 790, anchor = 'ne')

    kntsc15_inv = tk.Button(kntsc15, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    kntsc15_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc15_ext = tk.Button(kntsc15, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    kntsc15_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc15";')
    con.commit()

    kntsc15.mainloop()



def kntstr16():

    global kntsc16

    try:
        kntsc12.after(500, lambda: kntsc12.destroy())
    except NameError:
        pass

    try:
        kntsc14.after(500, lambda: kntsc14.destroy())
    except NameError:
        pass

    try:
        kntsc15.after(500, lambda: kntsc15.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc16 = tk.Toplevel()
    kntsc16.attributes('-fullscreen', True)
    kntsc16.configure(bd = 0)

    kntsc16_can = tk.Canvas(kntsc16, width = 1920, height = 1080, bg = 'black')
    kntsc16_can.pack(expand = True, fill = 'both')
    
    kbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 6.jpg'.format(kpath)))
    kntsc16_can.create_image(0, 0, image = kbg1, anchor = 'nw')

    kntsc16_pla = tk.Button(kntsc16, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc16_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc16_pau = tk.Button(kntsc16, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc16_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc16_inv = tk.Button(kntsc16, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7)
    kntsc16_inv.place(x = 1916, y = 890, anchor = 'ne')

    kntsc16_ext = tk.Button(kntsc16,text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    kntsc16_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc16";')
    con.commit()

    kntsc16.mainloop()



def kntstr17():
    
    global kntsc17

    try:
        kntsc12.after(500, lambda: kntsc12.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    kntsc17 = tk.Toplevel()
    kntsc17.attributes('-fullscreen', True)
    kntsc17.configure(bd = 1)

    kntsc17_can = tk.Canvas(kntsc17, width = 1920, height = 1080, bg = 'black')
    kntsc17_can.pack(expand = True, fill = 'both')
    
    kntsc17_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    kbg1 = ImageTk.PhotoImage(Image.open('{}Smoke.jpg'.format(ppath)))
    kntsc17_pic1 = tk.Label(kntsc17, image = kbg1, bd=5)
    kntsc17_pic1.place(x = 0, y = 0, anchor = 'nw')

    kbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 11.jpg'.format(kpath)))
    kntsc17_pic2 = tk.Label(kntsc17, image = kbg2, bd=5)
    kntsc17_pic2.place(x = 1320, y = 0, anchor = 'nw')

    kntsc17_fr1 = tk.Frame(kntsc17, width = 555, height = 365, bg = 'red')
    kntsc17_fr1.place(x = 15, y = 700, anchor = 'nw')
    kntsc17_fr1.propagate(0)

    kntsc17_opt1 = tk.Button(kntsc17_fr1, text = 'Poison\nthe Ogre Using a\nPoisoned Blade',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = kntstr14)
    kntsc17_opt1.pack(fill = 'both', expand = True)

    kntsc17_fr2 = tk.Frame(kntsc17, width = 555, height = 365, bg = 'blue')
    kntsc17_fr2.place(x = 575, y = 700, anchor = 'nw')
    kntsc17_fr2.propagate(0)

    kntsc17_opt2 = tk.Button(kntsc17_fr2, text = 'Paralyze\nthe Ogre\nUsing Chains',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = kntstr15)
    kntsc17_opt2.pack(fill = 'both', expand = True)

    kntsc17_fr3 = tk.Frame(kntsc17, width = 550, height = 363, bg = 'green')
    kntsc17_fr3.place(x = 1135, y = 700, anchor = 'nw')
    kntsc17_fr3.propagate(0)

    kntsc17_opt3 = tk.Button(kntsc17_fr3, text = 'Attack the Ogre\n with Your Knife',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = kntstr8)
    kntsc17_opt3.pack(fill = 'both', expand = True)

    kntsc17_pla = tk.Button(kntsc17, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    kntsc17_pla.place(x = 1865, y = 5, anchor = 'ne')

    kntsc17_pau = tk.Button(kntsc17, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    kntsc17_pau.place(x = 1915, y = 5, anchor = 'ne')

    kntsc17_heli = tk.Label(kntsc17, image = health_icn, bd = 0, bg = 'white')
    kntsc17_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    kntsc17_helt = tk.Label(kntsc17, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc17_helt.place(x = 1916, y = 690, anchor = 'ne')

    kntsc17_armi = tk.Label(kntsc17, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    kntsc17_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    kntsc17_armt = tk.Label(kntsc17, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    kntsc17_armt.place(x = 1916, y = 790, anchor = 'ne')

    kntsc17_inv = tk.Button(kntsc17, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    kntsc17_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    kntsc17_ext = tk.Button(kntsc17, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    kntsc17_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "kntsc17";')
    con.commit()

    kntsc17.mainloop()


#########################################################################################


## Monk's Story Begins ##

def mnkstr1():
    
    global mnksc1

    try:
        chrsc.after(500, lambda: chrsc.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc1 = tk.Toplevel()
    mnksc1.attributes('-fullscreen', True)
    mnksc1.configure(bd = 0)

    mnksc1_can = tk.Canvas(mnksc1, width = 1920, height = 1080, bg = 'black')
    mnksc1_can.pack(expand = True, fill = 'both')
    
    mbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 1.jpg'.format(mpath)))
    mnksc1_can.create_image(0, 0, image = mbg1, anchor = 'nw')

    mnksc1_lbl = tk.Label(mnksc1, text = 'Welcome {}!'.format(save_name),
                   font = ('Enchanted Land', 100, 'bold'), padx = 20,
                   bg = '#0F0F0F', fg = 'white', relief = 'groove',)
    mnksc1_lbl.place(x = 960, y = 20, anchor = 'n')

    mnksc1_pla = tk.Button(mnksc1, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc1_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc1_pau = tk.Button(mnksc1, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc1_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc1_inv = tk.Button(mnksc1, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=mnkstr2)
    mnksc1_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc1_ext = tk.Button(mnksc1, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    mnksc1_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc1";')
    con.commit()

    mnksc1.mainloop()

    
def mnkstr2():
    
    global mnksc2

    try:
        mnksc1.after(500, lambda: mnksc1.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc2 = tk.Toplevel()
    mnksc2.attributes('-fullscreen', True)
    mnksc2.configure(bd = 0)

    mnksc2_can = tk.Canvas(mnksc2, width = 1920, height = 1080, bg = 'black')
    mnksc2_can.pack(expand = True, fill = 'both')
    
    mbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 2.jpg'.format(mpath)))
    mnksc2_can.create_image(0, 0, image = mbg1, anchor = 'nw')

    mnksc2_pla = tk.Button(mnksc2, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc2_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc2_pau = tk.Button(mnksc2, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc2_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc2_inv = tk.Button(mnksc2, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=mnkstr3)
    mnksc2_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc2_ext = tk.Button(mnksc2, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    mnksc2_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc2";')
    con.commit()

    mnksc2.mainloop()


def mnkstr3():
    
    global mnksc3

    try:
        mnksc2.after(500, lambda: mnksc2.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc3 = tk.Toplevel()
    mnksc3.attributes('-fullscreen', True)
    mnksc3.configure(bd = 0)

    mnksc3_can = tk.Canvas(mnksc3, width = 1920, height = 1080, bg = 'black')
    mnksc3_can.pack(expand = True, fill = 'both')
    
    mbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 3.jpg'.format(mpath)))
    mnksc3_can.create_image(0, 0, image = mbg1, anchor = 'nw')

    mnksc3_pla = tk.Button(mnksc3, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc3_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc3_pau = tk.Button(mnksc3, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc3_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc3_inv = tk.Button(mnksc3, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=mnkstr4)
    mnksc3_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc3_ext = tk.Button(mnksc3, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    mnksc3_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc3";')
    con.commit()

    mnksc3.mainloop()


def mnkstr4():
    
    global mnksc4

    try:
        mnksc3.after(500, lambda: mnksc3.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc4 = tk.Toplevel()
    mnksc4.attributes('-fullscreen', True)
    mnksc4.configure(bd = 0)

    mnksc4_can = tk.Canvas(mnksc4, width = 1920, height = 1080, bg = 'black')
    mnksc4_can.pack(expand = True, fill = 'both')
    
    mbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 4.jpg'.format(mpath)))
    mnksc4_can.create_image(0, 0, image = mbg1, anchor = 'nw')

    mnksc4_pla = tk.Button(mnksc4, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc4_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc4_pau = tk.Button(mnksc4, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc4_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc4_inv = tk.Button(mnksc4, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=mnkstr5)
    mnksc4_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc4_ext = tk.Button(mnksc4, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    mnksc4_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc4";')
    con.commit()

    cur.execute('insert into stats values (100, 000);')
    con.commit()

    cur.execute('insert into inventory (item_name, quantity) values ("Knife", 1)')
    con.commit()

    cur.execute('insert into inventory (item_name, quantity) values ("Leftover Bread", 1)')
    con.commit()

    cur.execute('insert into inventory (item_name, quantity) values ("Gold Coins", 100)')
    con.commit()

    mnksc4.mainloop()



def mnkstr5():
    
    global mnksc5

    try:
        mnksc4.after(500, lambda: mnksc4.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    cur.execute('select health from stats;')
    health1 = cur.fetchall()
    health2 = health1[0]

    cur.execute('select armour from stats;')
    armour1 = cur.fetchall()
    armour2 = armour1[0]

    mnksc5 = tk.Toplevel()
    mnksc5.attributes('-fullscreen', True)
    mnksc5.configure(bd = 1)

    mnksc5_can = tk.Canvas(mnksc5, width = 1920, height = 1080, bg = 'black')
    mnksc5_can.pack(expand = True, fill = 'both')
    
    mnksc5_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    mbg1 = ImageTk.PhotoImage(Image.open('{}Prot\'s House.jpg'.format(ppath)))
    mnksc5_pic1 = tk.Label(mnksc5, image = mbg1, bd=5)
    mnksc5_pic1.place(x = 0, y = 0, anchor = 'nw')

    mbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 1.jpg'.format(mpath)))
    mnksc5_pic2 = tk.Label(mnksc5, image = mbg2, bd=5)
    mnksc5_pic2.place(x = 1320, y = 0, anchor = 'nw')

    mnksc5_fr1 = tk.Frame(mnksc5, width = 555, height = 365, bg = 'red')
    mnksc5_fr1.place(x = 15, y = 700, anchor = 'nw')
    mnksc5_fr1.propagate(0)

    mnksc5_opt1 = tk.Button(mnksc5_fr1, text = 'Horse \nCart',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white',command=mnkstr6)
    mnksc5_opt1.pack(fill = 'both', expand = True)

    mnksc5_fr2 = tk.Frame(mnksc5, width = 555, height = 365, bg = 'blue')
    mnksc5_fr2.place(x = 575, y = 700, anchor = 'nw')
    mnksc5_fr2.propagate(0)

    mnksc5_opt2 = tk.Button(mnksc5_fr2, text = 'On \nFoot',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white',command=mnkstr7)
    mnksc5_opt2.pack(fill = 'both', expand = True)

    mnksc5_fr3 = tk.Frame(mnksc5, width = 550, height = 363, bg = 'green')
    mnksc5_fr3.place(x = 1135, y = 700, anchor = 'nw')
    mnksc5_fr3.propagate(0)

    mnksc5_opt3 = tk.Button(mnksc5_fr3, text = 'Use a Vast\nTeleportation\nSpell',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white',command=mnkstr8)
    mnksc5_opt3.pack(fill = 'both', expand = True)

    mnksc5_pla = tk.Button(mnksc5, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc5_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc5_pau = tk.Button(mnksc5, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc5_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc5_fr4 = tk.Frame(mnksc5, width = 125, height = 105, bg = 'red')
    mnksc5_fr4.place(x = 1790, y = 690, anchor = 'nw')
    mnksc5_fr4.propagate(0)

    mnksc5_heli = tk.Label(mnksc5, image = health_icn, bd = 0, bg = 'white')
    mnksc5_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    mnksc5_helt = tk.Label(mnksc5_fr4, text = health2[0], font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc5_helt.pack(fill = 'both', expand = True)

    mnksc5_fr5 = tk.Frame(mnksc5, width = 125, height = 105, bg = 'red')
    mnksc5_fr5.place(x = 1790, y = 790, anchor = 'nw')
    mnksc5_fr5.propagate(0)

    mnksc5_armi = tk.Label(mnksc5, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    mnksc5_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    mnksc5_armt = tk.Label(mnksc5_fr5, text = armour2[0], font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc5_armt.pack(fill = 'both', expand = True)

    mnksc5_inv = tk.Button(mnksc5, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    mnksc5_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc5_ext = tk.Button(mnksc5, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    mnksc5_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc5";')
    con.commit()

    mnksc5.mainloop()


def mnkstr6():
    
    global mnksc6

    try:
        mnksc5.after(500, lambda: mnksc5.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc6 = tk.Toplevel()
    mnksc6.attributes('-fullscreen', True)
    mnksc6.configure(bd = 1)

    mnksc6_can = tk.Canvas(mnksc6, width = 1920, height = 1080, bg = 'black')
    mnksc6_can.pack(expand = True, fill = 'both')

    mnksc6_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    mbg1 = ImageTk.PhotoImage(Image.open('{}Ogre in a Jungle.jpg'.format(ppath)))
    mnksc6_pic1 = tk.Label(mnksc6, image = mbg1, bd=5)
    mnksc6_pic1.place(x = 0, y = 0, anchor = 'nw')

    mbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 2.jpg'.format(mpath)))
    mnksc6_pic2 = tk.Label(mnksc6, image = mbg2, bd=5)
    mnksc6_pic2.place(x = 1320, y = 0, anchor = 'nw')

    mnksc6_fr1 = tk.Frame(mnksc6, width = 555, height = 365, bg = 'red')
    mnksc6_fr1.place(x = 15, y = 700, anchor = 'nw')
    mnksc6_fr1.propagate(0)

    mnksc6_opt1 = tk.Button(mnksc6_fr1, font = ('Enchanted Land', 80),
                        text = 'Get off the Cart\n and Ask the \nRider to Leave',                            
                        bg = '#090D3A', fg = 'white', command = mnkstr9)
    mnksc6_opt1.pack(fill = 'both', expand = True)

    mnksc6_fr2 = tk.Frame(mnksc6, width = 555, height = 365, bg = 'blue')
    mnksc6_fr2.place(x = 575, y = 700, anchor = 'nw')
    mnksc6_fr2.propagate(0)

    mnksc6_opt2 = tk.Button(mnksc6_fr2, font = ('Enchanted Land', 80),
                            text = 'Get off the Cart \nand Hide Without\n Alerting the Rider',                            
                            bg = '#090D3A', fg = 'white', command = mnkstr10)
    mnksc6_opt2.pack(fill = 'both', expand = True)

    mnksc6_fr3 = tk.Frame(mnksc6, width = 550, height = 363, bg = 'green')
    mnksc6_fr3.place(x = 1135, y = 700, anchor = 'nw')
    mnksc6_fr3.propagate(0)

    mnksc6_opt3 = tk.Button(mnksc6_fr3, text = 'Attempt to Fight\n the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr11)
    mnksc6_opt3.pack(fill = 'both', expand = True)

    mnksc6_pla = tk.Button(mnksc6, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc6_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc6_pau = tk.Button(mnksc6, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc6_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc6_heli = tk.Label(mnksc6, image = health_icn, bd = 0, bg = 'white')
    mnksc6_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    mnksc6_helt = tk.Label(mnksc6, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc6_helt.place(x = 1916, y = 690, anchor = 'ne')

    mnksc6_armi = tk.Label(mnksc6, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    mnksc6_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    mnksc6_armt = tk.Label(mnksc6, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc6_armt.place(x = 1916, y = 790, anchor = 'ne')

    mnksc6_inv = tk.Button(mnksc6, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    mnksc6_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc6_ext = tk.Button(mnksc6, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    mnksc6_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc6";')
    con.commit()

    mnksc6.mainloop()



def mnkstr7():
    
    global mnksc7

    try:
        mnksc5.after(500, lambda: mnksc5.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass
    
    mnksc7 = tk.Toplevel()
    mnksc7.attributes('-fullscreen', True)
    mnksc7.configure(bd = 1)

    mnksc7_can = tk.Canvas(mnksc7, width = 1920, height = 1080, bg = 'black')
    mnksc7_can.pack(expand = True, fill = 'both')

    mnksc7_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    mbg1 = ImageTk.PhotoImage(Image.open('{}Ogre in a Jungle.jpg'.format(ppath)))
    mnksc7_pic1 = tk.Label(mnksc7, image = mbg1, bd=5)
    mnksc7_pic1.place(x = 0, y = 0, anchor = 'nw')

    mbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 3.jpg'.format(mpath)))
    mnksc7_pic2 = tk.Label(mnksc7, image = mbg2, bd=5)
    mnksc7_pic2.place(x = 1320, y = 0, anchor = 'nw')

    mnksc7_fr1 = tk.Frame(mnksc7, width = 555, height = 365, bg = 'red')
    mnksc7_fr1.place(x = 15, y = 700, anchor = 'nw')
    mnksc7_fr1.propagate(0)

    mnksc7_opt1 = tk.Button(mnksc7_fr1, text = 'Attempt to\n Distract the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr12)
    mnksc7_opt1.pack(fill = 'both', expand = True)

    mnksc7_fr2 = tk.Frame(mnksc7, width = 555, height = 365, bg = 'blue')
    mnksc7_fr2.place(x = 575, y = 700, anchor = 'nw')
    mnksc7_fr2.propagate(0)

    mnksc7_opt2 = tk.Button(mnksc7_fr2, text = 'Attempt to\n Fight the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr11)
    mnksc7_opt2.pack(fill = 'both', expand = True)

    mnksc7_fr3 = tk.Frame(mnksc7, width = 550, height = 363, bg = 'green')
    mnksc7_fr3.place(x = 1135, y = 700, anchor = 'nw')
    mnksc7_fr3.propagate(0)

    mnksc7_opt3 = tk.Button(mnksc7_fr3, text = 'Hide and Hope\n that the Ogre\n Goes Away',
                        font = ('Enchanted Land', 80),
                        bg = '#090D3A', fg = 'white', command = mnkstr13)
    mnksc7_opt3.pack(fill = 'both', expand = True)

    mnksc7_pla = tk.Button(mnksc7, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc7_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc7_pau = tk.Button(mnksc7, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc7_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc7_heli = tk.Label(mnksc7, image = health_icn, bd = 0, bg = 'white')
    mnksc7_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    mnksc7_helt = tk.Label(mnksc7, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc7_helt.place(x = 1916, y = 690, anchor = 'ne')

    mnksc7_armi = tk.Label(mnksc7, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    mnksc7_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    mnksc7_armt = tk.Label(mnksc7, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc7_armt.place(x = 1916, y = 790, anchor = 'ne')

    mnksc7_inv = tk.Button(mnksc7, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    mnksc7_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc7_ext = tk.Button(mnksc7, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    mnksc7_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc7";')
    con.commit()

    mnksc7.mainloop()



def mnkstr8():
    
    global mnksc8

    try:
        mnksc5.after(500, lambda: mnksc5.destroy())
    except NameError:
        pass

    try:
        mnksc11.after(500, lambda: mnksc11.destroy())
    except NameError:
        pass

    try:
        mnksc12.after(500, lambda: mnksc12.destroy())
    except NameError:
        pass

    try:
        mnksc13.after(500, lambda: mnksc13.destroy())
    except NameError:
        pass

    try:
        mnksc14.after(500, lambda: mnksc14.destroy())
    except NameError:
        pass

    try:
        mnksc15.after(500, lambda: mnksc15.destroy())
    except NameError:
        pass

    try:
        mnksc17.after(500, lambda: mnksc17.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc8 = tk.Toplevel()
    mnksc8.attributes('-fullscreen', True)
    mnksc8.configure(bd = 0)

    mnksc8_can = tk.Canvas(mnksc8, width = 1920, height = 1080, bg = 'black')
    mnksc8_can.pack(expand = True, fill = 'both')
    
    mbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 5.jpg'.format(mpath)))
    mnksc8_can.create_image(0, 0, image = mbg1, anchor = 'nw')

    mnksc8_pla = tk.Button(mnksc8, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc8_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc8_pau = tk.Button(mnksc8, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc8_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc8_ext = tk.Button(mnksc8, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    mnksc8_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc8";')
    con.commit()

    mnksc8.mainloop()



def mnkstr9():
    
    global mnksc9

    try:
        mnksc6.after(500, lambda: mnksc6.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc9 = tk.Toplevel()
    mnksc9.attributes('-fullscreen', True)
    mnksc9.configure(bd = 1)

    mnksc9_can = tk.Canvas(mnksc9, width = 1920, height = 1080, bg = 'black')
    mnksc9_can.pack(expand = True, fill = 'both')

    mnksc9_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    mbg1 = ImageTk.PhotoImage(Image.open('{}Horsecart 1.jpg'.format(ppath)))
    mnksc9_pic1 = tk.Label(mnksc9, image = mbg1, bd=5)
    mnksc9_pic1.place(x = 0, y = 0, anchor = 'nw')

    mbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 4.jpg'.format(mpath)))
    mnksc9_pic2 = tk.Label(mnksc9, image = mbg2, bd=5)
    mnksc9_pic2.place(x = 1320, y = 0, anchor = 'nw')

    mnksc9_fr1 = tk.Frame(mnksc9, width = 555, height = 365, bg = 'red')
    mnksc9_fr1.place(x = 15, y = 700, anchor = 'nw')
    mnksc9_fr1.propagate(0)

    mnksc9_opt1 = tk.Button(mnksc9_fr1, text = 'Attempt to\n Distract the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr12)
    mnksc9_opt1.pack(fill = 'both', expand = True)

    mnksc9_fr2 = tk.Frame(mnksc9, width = 555, height = 365, bg = 'blue')
    mnksc9_fr2.place(x = 575, y = 700, anchor = 'nw')
    mnksc9_fr2.propagate(0)

    mnksc9_opt2 = tk.Button(mnksc9_fr2, text = 'Attempt to\n Fight the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr11)
    mnksc9_opt2.pack(fill = 'both', expand = True)

    mnksc9_fr3 = tk.Frame(mnksc9, width = 550, height = 363, bg = 'green')
    mnksc9_fr3.place(x = 1135, y = 700, anchor = 'nw')
    mnksc9_fr3.propagate(0)

    mnksc9_opt3 = tk.Button(mnksc9_fr3, text = 'Hide and Hope\nthat the Ogre\nGoes Away',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr13)
    mnksc9_opt3.pack(fill = 'both', expand = True)

    mnksc9_pla = tk.Button(mnksc9, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc9_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc9_pau = tk.Button(mnksc9, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc9_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc9_heli = tk.Label(mnksc9, image = health_icn, bd = 0, bg = 'white')
    mnksc9_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    mnksc9_helt = tk.Label(mnksc9, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc9_helt.place(x = 1916, y = 690, anchor = 'ne')

    mnksc9_armi = tk.Label(mnksc9, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    mnksc9_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    mnksc9_armt = tk.Label(mnksc9, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc9_armt.place(x = 1916, y = 790, anchor = 'ne')

    mnksc9_inv = tk.Button(mnksc9, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    mnksc9_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc9_ext = tk.Button(mnksc9, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    mnksc9_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc9";')
    con.commit()

    mnksc9.mainloop()



def mnkstr10():
    
    global mnksc10

    try:
        mnksc6.after(500, lambda: mnksc6.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc10 = tk.Toplevel()
    mnksc10.attributes('-fullscreen', True)
    mnksc10.configure(bd = 1)

    mnksc10_can = tk.Canvas(mnksc10, width = 1920, height = 1080, bg = 'black')
    mnksc10_can.pack(expand = True, fill = 'both')

    mnksc10_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    mbg1 = ImageTk.PhotoImage(Image.open('{}Wagon.jpg'.format(ppath)))
    mnksc10_pic1 = tk.Label(mnksc10, image = mbg1, bd=5)
    mnksc10_pic1.place(x = 0, y = 0, anchor = 'nw')

    mbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 5.jpg'.format(mpath)))
    mnksc10_pic2 = tk.Label(mnksc10, image = mbg2, bd=5)
    mnksc10_pic2.place(x = 1320, y = 0, anchor = 'nw')

    mnksc10_fr1 = tk.Frame(mnksc10, width = 555, height = 365, bg = 'red')
    mnksc10_fr1.place(x = 15, y = 700, anchor = 'nw')
    mnksc10_fr1.propagate(0)

    mnksc10_opt1 = tk.Button(mnksc10_fr1, text = 'Attempt to\n Distract the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr12)
    mnksc10_opt1.pack(fill = 'both', expand = True)

    mnksc10_fr2 = tk.Frame(mnksc10, width = 555, height = 365, bg = 'blue')
    mnksc10_fr2.place(x = 575, y = 700, anchor = 'nw')
    mnksc10_fr2.propagate(0)

    mnksc10_opt2 = tk.Button(mnksc10_fr2, text = 'Attempt to\n Fight the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr11)
    mnksc10_opt2.pack(fill = 'both', expand = True)

    mnksc10_fr3 = tk.Frame(mnksc10, width = 550, height = 363, bg = 'green')
    mnksc10_fr3.place(x = 1135, y = 700, anchor = 'nw')
    mnksc10_fr3.propagate(0)

    mnksc10_opt3 = tk.Button(mnksc10_fr3, text = 'Hide and Hope\n that the Ogre\n Goes Away',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr13)
    mnksc10_opt3.pack(fill = 'both', expand = True)

    mnksc10_pla = tk.Button(mnksc10, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc10_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc10_pau = tk.Button(mnksc10, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc10_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc10_heli = tk.Label(mnksc10, image = health_icn, bd = 0, bg = 'white')
    mnksc10_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    mnksc10_helt = tk.Label(mnksc10, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc10_helt.place(x = 1916, y = 690, anchor = 'ne')

    mnksc10_armi = tk.Label(mnksc10, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    mnksc10_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    mnksc10_armt = tk.Label(mnksc10, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc10_armt.place(x = 1916, y = 790, anchor = 'ne')

    mnksc10_inv = tk.Button(mnksc10, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    mnksc10_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc10_ext = tk.Button(mnksc10, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    mnksc10_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc10";')
    con.commit()

    mnksc10.mainloop()



def mnkstr11():
    
    global mnksc11

    try:
        mnksc6.after(500, lambda: mnksc6.destroy())
    except NameError:
        pass

    try:
        mnksc7.after(500, lambda: mnksc7.destroy())
    except NameError:
        pass

    try:
        mnksc9.after(500, lambda: mnksc9.destroy())
    except NameError:
        pass

    try:
        mnksc10.after(500, lambda: mnksc10.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc11 = tk.Toplevel()
    mnksc11.attributes('-fullscreen', True)
    mnksc11.configure(bd = 1)

    mnksc11_can = tk.Canvas(mnksc11, width = 1920, height = 1080, bg = 'black')
    mnksc11_can.pack(expand = True, fill = 'both')

    mnksc11_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    mbg1 = ImageTk.PhotoImage(Image.open('{}Ogre Fight.jpg'.format(ppath)))
    mnksc11_pic1 = tk.Label(mnksc11, image = mbg1, bd=5)
    mnksc11_pic1.place(x = 0, y = 0, anchor = 'nw')

    mbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 6.jpg'.format(mpath)))
    mnksc11_pic2 = tk.Label(mnksc11, image = mbg2, bd=5)
    mnksc11_pic2.place(x = 1320, y = 0, anchor = 'nw')

    mnksc11_fr1 = tk.Frame(mnksc11, width = 555, height = 365, bg = 'red')
    mnksc11_fr1.place(x = 15, y = 700, anchor = 'nw')
    mnksc11_fr1.propagate(0)

    mnksc11_opt1 = tk.Button(mnksc11_fr1, text = 'Poison\nthe Ogre',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = mnkstr14)
    mnksc11_opt1.pack(fill = 'both', expand = True)

    mnksc11_fr2 = tk.Frame(mnksc11, width = 555, height = 365, bg = 'blue')
    mnksc11_fr2.place(x = 575, y = 700, anchor = 'nw')
    mnksc11_fr2.propagate(0)

    mnksc11_opt2 = tk.Button(mnksc11_fr2, text = 'Paralyze\nthe Ogre',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = mnkstr15)
    mnksc11_opt2.pack(fill = 'both', expand = True)

    mnksc11_fr3 = tk.Frame(mnksc11, width = 550, height = 363, bg = 'green')
    mnksc11_fr3.place(x = 1135, y = 700, anchor = 'nw')
    mnksc11_fr3.propagate(0)

    mnksc11_opt3 = tk.Button(mnksc11_fr3, text = 'Use Your Knife\n to Attack',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr8)
    mnksc11_opt3.pack(fill = 'both', expand = True)

    mnksc11_pla = tk.Button(mnksc11, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc11_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc11_pau = tk.Button(mnksc11, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc11_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc11_heli = tk.Label(mnksc11, image = health_icn, bd = 0, bg = 'white')
    mnksc11_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    mnksc11_helt = tk.Label(mnksc11, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc11_helt.place(x = 1916, y = 690, anchor = 'ne')

    mnksc11_armi = tk.Label(mnksc11, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    mnksc11_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    mnksc11_armt = tk.Label(mnksc11, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc11_armt.place(x = 1916, y = 790, anchor = 'ne')

    mnksc11_inv = tk.Button(mnksc11, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    mnksc11_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc11_ext = tk.Button(mnksc11, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    mnksc11_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc11";')
    con.commit()

    mnksc11.mainloop()



def mnkstr12():
    
    global mnksc12

    try:
        mnksc7.after(500, lambda: mnksc7.destroy())
    except NameError:
        pass

    try:
        mnksc9.after(500, lambda: mnksc9.destroy())
    except NameError:
        pass

    try:
        mnksc10.after(500, lambda: mnksc10.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc12 = tk.Toplevel()
    mnksc12.attributes('-fullscreen', True)
    mnksc12.configure(bd = 1)

    mnksc12_can = tk.Canvas(mnksc12, width = 1920, height = 1080, bg = 'black')
    mnksc12_can.pack(expand = True, fill = 'both')

    mnksc12_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    mbg1 = ImageTk.PhotoImage(Image.open('{}Wizard Story.jpg'.format(ppath)))
    mnksc12_pic1 = tk.Label(mnksc12, image = mbg1, bd=5)
    mnksc12_pic1.place(x = 0, y = 0, anchor = 'nw')

    mbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 7.jpg'.format(mpath)))
    mnksc12_pic2 = tk.Label(mnksc12, image = mbg2, bd=5)
    mnksc12_pic2.place(x = 1320, y = 0, anchor = 'nw')

    mnksc12_fr1 = tk.Frame(mnksc12, width = 555, height = 365, bg = 'red')
    mnksc12_fr1.place(x = 15, y = 700, anchor = 'nw')
    mnksc12_fr1.propagate(0)

    mnksc12_opt1 = tk.Button(mnksc12_fr1, font = ('Enchanted Land', 55),
                             text = 'Make a Clone of Yourself\nand Have it Distract\n the Ogre by Running\n Away from You',
                             bg = '#090D3A', fg = 'white', command = mnkstr16)
    mnksc12_opt1.pack(fill = 'both', expand = True)

    mnksc12_fr2 = tk.Frame(mnksc12, width = 555, height = 365, bg = 'blue')
    mnksc12_fr2.place(x = 575, y = 700, anchor = 'nw')
    mnksc12_fr2.propagate(0)

    mnksc12_opt2 = tk.Button(mnksc12_fr2, text = 'Cast a Spell to Cover\nthe Surroundings\n in Smoke',
                            font = ('Enchanted Land', 70),
                            bg = '#090D3A', fg = 'white', command = mnkstr17)
    mnksc12_opt2.pack(fill = 'both', expand = True)

    mnksc12_fr3 = tk.Frame(mnksc12, width = 550, height = 363, bg = 'green')
    mnksc12_fr3.place(x = 1135, y = 700, anchor = 'nw')
    mnksc12_fr3.propagate(0)

    mnksc12_opt3 = tk.Button(mnksc12_fr3, text = 'Throw a Big Rock\n in the Lake Nearby',
                            font = ('Enchanted Land', 75),
                            bg = '#090D3A', fg = 'white', command = mnkstr8)
    mnksc12_opt3.pack(fill = 'both', expand = True)

    mnksc12_pla = tk.Button(mnksc12, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc12_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc12_pau = tk.Button(mnksc12, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc12_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc12_heli = tk.Label(mnksc12, image = health_icn, bd = 0, bg = 'white')
    mnksc12_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    mnksc12_helt = tk.Label(mnksc12, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc12_helt.place(x = 1916, y = 690, anchor = 'ne')

    mnksc12_armi = tk.Label(mnksc12, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    mnksc12_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    mnksc12_armt = tk.Label(mnksc12, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc12_armt.place(x = 1916, y = 790, anchor = 'ne')

    mnksc12_inv = tk.Button(mnksc12, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    mnksc12_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc12_ext = tk.Button(mnksc12, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    mnksc12_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc12";')
    con.commit()

    mnksc12.mainloop()




def mnkstr13():
    
    global mnksc13

    try:
        mnksc7.after(500, lambda: mnksc7.destroy())
    except NameError:
        pass

    try:
        mnksc9.after(500, lambda: mnksc9.destroy())
    except NameError:
        pass

    try:
        mnksc10.after(500, lambda: mnksc10.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc13 = tk.Toplevel()
    mnksc13.attributes('-fullscreen', True)
    mnksc13.configure(bd = 1)

    mnksc13_can = tk.Canvas(mnksc13, width = 1920, height = 1080, bg = 'black')
    mnksc13_can.pack(expand = True, fill = 'both')

    mnksc13_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    mbg1 = ImageTk.PhotoImage(Image.open('{}Ogre Fight.jpg'.format(ppath)))
    mnksc13_pic1 = tk.Label(mnksc13, image = mbg1, bd=5)
    mnksc13_pic1.place(x = 0, y = 0, anchor = 'nw')

    mbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 8.jpg'.format(mpath)))
    mnksc13_pic2 = tk.Label(mnksc13, image = mbg2, bd=5)
    mnksc13_pic2.place(x = 1320, y = 0, anchor = 'nw')

    mnksc13_fr1 = tk.Frame(mnksc13, width = 555, height = 365, bg = 'red')
    mnksc13_fr1.place(x = 15, y = 700, anchor = 'nw')
    mnksc13_fr1.propagate(0)

    mnksc13_opt1 = tk.Button(mnksc13_fr1, text = 'Poison\nthe Ogre',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = mnkstr14)
    mnksc13_opt1.pack(fill = 'both', expand = True)

    mnksc13_fr2 = tk.Frame(mnksc13, width = 555, height = 365, bg = 'blue')
    mnksc13_fr2.place(x = 575, y = 700, anchor = 'nw')
    mnksc13_fr2.propagate(0)

    mnksc13_opt2 = tk.Button(mnksc13_fr2, text = 'Paralyze\nthe Ogre',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = mnkstr15)
    mnksc13_opt2.pack(fill = 'both', expand = True)

    mnksc13_fr3 = tk.Frame(mnksc13, width = 550, height = 363, bg = 'green')
    mnksc13_fr3.place(x = 1135, y = 700, anchor = 'nw')
    mnksc13_fr3.propagate(0)

    mnksc13_opt3 = tk.Button(mnksc13_fr3, text = 'Try to Stab\n the Ogre with\n Your Knife',
                            font = ('Enchanted Land', 70),
                            bg = '#090D3A', fg = 'white', command = mnkstr8)
    mnksc13_opt3.pack(fill = 'both', expand = True)

    mnksc13_pla = tk.Button(mnksc13, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc13_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc13_pau = tk.Button(mnksc13, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc13_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc13_heli = tk.Label(mnksc13, image = health_icn, bd = 0, bg = 'white')
    mnksc13_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    mnksc13_helt = tk.Label(mnksc13, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc13_helt.place(x = 1916, y = 690, anchor = 'ne')

    mnksc13_armi = tk.Label(mnksc13, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    mnksc13_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    mnksc13_armt = tk.Label(mnksc13, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc13_armt.place(x = 1916, y = 790, anchor = 'ne')

    mnksc13_inv = tk.Button(mnksc13, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    mnksc13_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc13_ext = tk.Button(mnksc13, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    mnksc13_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc13";')
    con.commit()

    mnksc13.mainloop()



def mnkstr14():
    
    global mnksc14

    try:
        mnksc11.after(500, lambda: mnksc11.destroy())
    except NameError:
        pass

    try:
        mnksc13.after(500, lambda: mnksc13.destroy())
    except NameError:
        pass

    try:
        mnksc17.after(500, lambda: mnksc17.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc14 = tk.Toplevel()
    mnksc14.attributes('-fullscreen', True)
    mnksc14.configure(bd = 1)

    mnksc14_can = tk.Canvas(mnksc14, width = 1920, height = 1080, bg = 'black')
    mnksc14_can.pack(expand = True, fill = 'both')
    
    mnksc14_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    mbg1 = ImageTk.PhotoImage(Image.open('{}Poison.jpg'.format(ppath)))
    mnksc14_pic1 = tk.Label(mnksc14, image = mbg1, bd=5)
    mnksc14_pic1.place(x = 0, y = 0, anchor = 'nw')

    mbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 9.jpg'.format(mpath)))
    mnksc14_pic2 = tk.Label(mnksc14, image = mbg2, bd=5)
    mnksc14_pic2.place(x = 1320, y = 0, anchor = 'nw')

    mnksc14_fr1 = tk.Frame(mnksc14, width = 555, height = 365, bg = 'red')
    mnksc14_fr1.place(x = 15, y = 700, anchor = 'nw')
    mnksc14_fr1.propagate(0)

    mnksc14_opt1 = tk.Button(mnksc14_fr1, text = 'Knock it\nUnconcious\n with Your Staff',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr16)
    mnksc14_opt1.pack(fill = 'both', expand = True)

    mnksc14_fr2 = tk.Frame(mnksc14, width = 555, height = 365, bg = 'blue')
    mnksc14_fr2.place(x = 575, y = 700, anchor = 'nw')
    mnksc14_fr2.propagate(0)

    mnksc14_opt2 = tk.Button(mnksc14_fr2, text = 'Use Your Knife to\nPut an End to\n the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr16)
    mnksc14_opt2.pack(fill = 'both', expand = True)

    mnksc14_fr3 = tk.Frame(mnksc14, width = 550, height = 363, bg = 'green')
    mnksc14_fr3.place(x = 1135, y = 700, anchor = 'nw')
    mnksc14_fr3.propagate(0)

    mnksc14_opt3 = tk.Button(mnksc14_fr3, text = 'Leave the Ogre\n and Let Time Put\n an End to it',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr8)
    mnksc14_opt3.pack(fill = 'both', expand = True)

    mnksc14_pla = tk.Button(mnksc14, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc14_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc14_pau = tk.Button(mnksc14, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc14_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc14_heli = tk.Label(mnksc14, image = health_icn, bd = 0, bg = 'white')
    mnksc14_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    mnksc14_helt = tk.Label(mnksc14, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc14_helt.place(x = 1916, y = 690, anchor = 'ne')

    mnksc14_armi = tk.Label(mnksc14, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    mnksc14_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    mnksc14_armt = tk.Label(mnksc14, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc14_armt.place(x = 1916, y = 790, anchor = 'ne')

    mnksc14_inv = tk.Button(mnksc14, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    mnksc14_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc14_ext = tk.Button(mnksc14, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    mnksc14_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc14";')
    con.commit()

    mnksc14.mainloop()



def mnkstr15():
    
    global mnksc15

    try:
        mnksc11.after(500, lambda: mnksc11.destroy())
    except NameError:
        pass

    try:
        mnksc13.after(500, lambda: mnksc13.destroy())
    except NameError:
        pass

    try:
        mnksc17.after(500, lambda: mnksc17.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc15 = tk.Toplevel()
    mnksc15.attributes('-fullscreen', True)
    mnksc15.configure(bd = 1)

    mnksc15_can = tk.Canvas(mnksc15, width = 1920, height = 1080, bg = 'black')
    mnksc15_can.pack(expand = True, fill = 'both')
    
    mnksc15_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    mbg1 = ImageTk.PhotoImage(Image.open('{}Chains.jpg'.format(ppath)))
    mnksc15_pic1 = tk.Label(mnksc15, image = mbg1, bd=5)
    mnksc15_pic1.place(x = 0, y = 0, anchor = 'nw')

    mbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 10.jpg'.format(mpath)))
    mnksc15_pic2 = tk.Label(mnksc15, image = mbg2, bd=5)
    mnksc15_pic2.place(x = 1320, y = 0, anchor = 'nw')

    mnksc15_fr1 = tk.Frame(mnksc15, width = 555, height = 365, bg = 'red')
    mnksc15_fr1.place(x = 15, y = 700, anchor = 'nw')
    mnksc15_fr1.propagate(0)

    mnksc15_opt1 = tk.Button(mnksc15_fr1, text = 'Knock it\nUnconcious\n with Your Staff',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr16)
    mnksc15_opt1.pack(fill = 'both', expand = True)

    mnksc15_fr2 = tk.Frame(mnksc15, width = 555, height = 365, bg = 'blue')
    mnksc15_fr2.place(x = 575, y = 700, anchor = 'nw')
    mnksc15_fr2.propagate(0)

    mnksc15_opt2 = tk.Button(mnksc15_fr2, text = 'Use Your Knife\nto Put an End\nto the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr16)
    mnksc15_opt2.pack(fill = 'both', expand = True)

    mnksc15_fr3 = tk.Frame(mnksc15, width = 550, height = 363, bg = 'green')
    mnksc15_fr3.place(x = 1135, y = 700, anchor = 'nw')
    mnksc15_fr3.propagate(0)

    mnksc15_opt3 = tk.Button(mnksc15_fr3, text = 'Make a\nRun for it',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = mnkstr8)
    mnksc15_opt3.pack(fill = 'both', expand = True)

    mnksc15_pla = tk.Button(mnksc15, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc15_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc15_pau = tk.Button(mnksc15, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc15_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc15_heli = tk.Label(mnksc15, image = health_icn, bd = 0, bg = 'white')
    mnksc15_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    mnksc15_helt = tk.Label(mnksc15, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc15_helt.place(x = 1916, y = 690, anchor = 'ne')

    mnksc15_armi = tk.Label(mnksc15, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    mnksc15_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    mnksc15_armt = tk.Label(mnksc15, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc15_armt.place(x = 1916, y = 790, anchor = 'ne')

    mnksc15_inv = tk.Button(mnksc15, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    mnksc15_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc15_ext = tk.Button(mnksc15, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    mnksc15_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc15";')
    con.commit()

    mnksc15.mainloop()



def mnkstr16():

    global mnksc16

    try:
        mnksc12.after(500, lambda: mnksc12.destroy())
    except NameError:
        pass

    try:
        mnksc14.after(500, lambda: mnksc14.destroy())
    except NameError:
        pass

    try:
        mnksc15.after(500, lambda: mnksc15.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc16 = tk.Toplevel()
    mnksc16.attributes('-fullscreen', True)
    mnksc16.configure(bd = 0)

    mnksc16_can = tk.Canvas(mnksc16, width = 1920, height = 1080, bg = 'black')
    mnksc16_can.pack(expand = True, fill = 'both')
    
    mbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 6.jpg'.format(mpath)))
    mnksc16_can.create_image(0, 0, image = mbg1, anchor = 'nw')

    mnksc16_pla = tk.Button(mnksc16, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc16_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc16_pau = tk.Button(mnksc16, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc16_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc16_inv = tk.Button(mnksc16, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7)
    mnksc16_inv.place(x = 1916, y = 890, anchor = 'ne')

    mnksc16_ext = tk.Button(mnksc16,text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    mnksc16_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc16";')
    con.commit()

    mnksc16.mainloop()



def mnkstr17():
    
    global mnksc17

    try:
        mnksc12.after(500, lambda: mnksc12.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    mnksc17 = tk.Toplevel()
    mnksc17.attributes('-fullscreen', True)
    mnksc17.configure(bd = 1)

    mnksc17_can = tk.Canvas(mnksc17, width = 1920, height = 1080, bg = 'black')
    mnksc17_can.pack(expand = True, fill = 'both')
    
    mnksc17_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    mbg1 = ImageTk.PhotoImage(Image.open('{}Smoke.jpg'.format(ppath)))
    mnksc17_pic1 = tk.Label(mnksc17, image = mbg1, bd=5)
    mnksc17_pic1.place(x = 0, y = 0, anchor = 'nw')

    mbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 11.jpg'.format(mpath)))
    mnksc17_pic2 = tk.Label(mnksc17, image = mbg2, bd=5)
    mnksc17_pic2.place(x = 1320, y = 0, anchor = 'nw')

    mnksc17_fr1 = tk.Frame(mnksc17, width = 555, height = 365, bg = 'red')
    mnksc17_fr1.place(x = 15, y = 700, anchor = 'nw')
    mnksc17_fr1.propagate(0)

    mnksc17_opt1 = tk.Button(mnksc17_fr1, text = 'Poison\nthe Ogre',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = mnkstr14)
    mnksc17_opt1.pack(fill = 'both', expand = True)

    mnksc17_fr2 = tk.Frame(mnksc17, width = 555, height = 365, bg = 'blue')
    mnksc17_fr2.place(x = 575, y = 700, anchor = 'nw')
    mnksc17_fr2.propagate(0)

    mnksc17_opt2 = tk.Button(mnksc17_fr2, text = 'Paralyze\nthe Ogre',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = mnkstr15)
    mnksc17_opt2.pack(fill = 'both', expand = True)

    mnksc17_fr3 = tk.Frame(mnksc17, width = 550, height = 363, bg = 'green')
    mnksc17_fr3.place(x = 1135, y = 700, anchor = 'nw')
    mnksc17_fr3.propagate(0)

    mnksc17_opt3 = tk.Button(mnksc17_fr3, text = 'Attack the Ogre\n with Your Knife',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = mnkstr8)
    mnksc17_opt3.pack(fill = 'both', expand = True)

    mnksc17_pla = tk.Button(mnksc17, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    mnksc17_pla.place(x = 1865, y = 5, anchor = 'ne')

    mnksc17_pau = tk.Button(mnksc17, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    mnksc17_pau.place(x = 1915, y = 5, anchor = 'ne')

    mnksc17_heli = tk.Label(mnksc17, image = health_icn, bd = 0, bg = 'white')
    mnksc17_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    mnksc17_helt = tk.Label(mnksc17, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc17_helt.place(x = 1916, y = 690, anchor = 'ne')

    mnksc17_armi = tk.Label(mnksc17, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    mnksc17_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    mnksc17_armt = tk.Label(mnksc17, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    mnksc17_armt.place(x = 1916, y = 790, anchor = 'ne')

    mnksc17_inv = tk.Button(mnksc17, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    mnksc17_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    mnksc17_ext = tk.Button(mnksc17, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    mnksc17_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "mnksc17";')
    con.commit()

    mnksc17.mainloop()


#########################################################################################


## Thief's Story Begins ##

def thfstr1():
    
    global thfsc1

    try:
        chrsc.after(500, lambda: chrsc.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc1 = tk.Toplevel()
    thfsc1.attributes('-fullscreen', True)
    thfsc1.configure(bd = 0)

    thfsc1_can = tk.Canvas(thfsc1, width = 1920, height = 1080, bg = 'black')
    thfsc1_can.pack(expand = True, fill = 'both')
    
    tbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 1.jpg'.format(tpath)))
    thfsc1_can.create_image(0, 0, image = tbg1, anchor = 'nw')

    thfsc1_lbl = tk.Label(thfsc1, text = 'Welcome {}!'.format(save_name),
                   font = ('Enchanted Land', 100, 'bold'), padx = 20,
                   bg = '#0F0F0F', fg = 'white', relief = 'groove',)
    thfsc1_lbl.place(x = 960, y = 20, anchor = 'n')

    thfsc1_pla = tk.Button(thfsc1, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc1_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc1_pau = tk.Button(thfsc1, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc1_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc1_inv = tk.Button(thfsc1, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=thfstr2)
    thfsc1_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc1_ext = tk.Button(thfsc1, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    thfsc1_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc1";')
    con.commit()

    thfsc1.mainloop()

    
def thfstr2():
    
    global thfsc2

    try:
        thfsc1.after(500, lambda: thfsc1.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc2 = tk.Toplevel()
    thfsc2.attributes('-fullscreen', True)
    thfsc2.configure(bd = 0)

    thfsc2_can = tk.Canvas(thfsc2, width = 1920, height = 1080, bg = 'black')
    thfsc2_can.pack(expand = True, fill = 'both')
    
    tbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 2.jpg'.format(tpath)))
    thfsc2_can.create_image(0, 0, image = tbg1, anchor = 'nw')

    thfsc2_pla = tk.Button(thfsc2, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc2_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc2_pau = tk.Button(thfsc2, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc2_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc2_inv = tk.Button(thfsc2, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=thfstr3)
    thfsc2_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc2_ext = tk.Button(thfsc2, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    thfsc2_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc2";')
    con.commit()

    thfsc2.mainloop()


def thfstr3():
    
    global thfsc3

    try:
        thfsc2.after(500, lambda: thfsc2.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc3 = tk.Toplevel()
    thfsc3.attributes('-fullscreen', True)
    thfsc3.configure(bd = 0)

    thfsc3_can = tk.Canvas(thfsc3, width = 1920, height = 1080, bg = 'black')
    thfsc3_can.pack(expand = True, fill = 'both')
    
    tbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 3.jpg'.format(tpath)))
    thfsc3_can.create_image(0, 0, image = tbg1, anchor = 'nw')

    thfsc3_pla = tk.Button(thfsc3, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc3_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc3_pau = tk.Button(thfsc3, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc3_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc3_inv = tk.Button(thfsc3, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=thfstr4)
    thfsc3_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc3_ext = tk.Button(thfsc3, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    thfsc3_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc3";')
    con.commit()

    thfsc3.mainloop()


def thfstr4():
    
    global thfsc4

    try:
        thfsc3.after(500, lambda: thfsc3.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc4 = tk.Toplevel()
    thfsc4.attributes('-fullscreen', True)
    thfsc4.configure(bd = 0)

    thfsc4_can = tk.Canvas(thfsc4, width = 1920, height = 1080, bg = 'black')
    thfsc4_can.pack(expand = True, fill = 'both')
    
    tbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 4.jpg'.format(tpath)))
    thfsc4_can.create_image(0, 0, image = tbg1, anchor = 'nw')

    thfsc4_pla = tk.Button(thfsc4, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc4_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc4_pau = tk.Button(thfsc4, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc4_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc4_inv = tk.Button(thfsc4, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=thfstr5)
    thfsc4_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc4_ext = tk.Button(thfsc4, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    thfsc4_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc4";')
    con.commit()

    cur.execute('insert into stats values (100, 000);')
    con.commit()

    cur.execute('insert into inventory (item_name, quantity) values ("Knife", 1)')
    con.commit()

    cur.execute('insert into inventory (item_name, quantity) values ("Leftover Bread", 1)')
    con.commit()

    cur.execute('insert into inventory (item_name, quantity) values ("Gold Coins", 100)')
    con.commit()

    thfsc4.mainloop()



def thfstr5():
    
    global thfsc5

    try:
        thfsc4.after(500, lambda: thfsc4.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    cur.execute('select health from stats;')
    health1 = cur.fetchall()
    health2 = health1[0]

    cur.execute('select armour from stats;')
    armour1 = cur.fetchall()
    armour2 = armour1[0]

    thfsc5 = tk.Toplevel()
    thfsc5.attributes('-fullscreen', True)
    thfsc5.configure(bd = 1)

    thfsc5_can = tk.Canvas(thfsc5, width = 1920, height = 1080, bg = 'black')
    thfsc5_can.pack(expand = True, fill = 'both')
    
    thfsc5_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    tbg1 = ImageTk.PhotoImage(Image.open('{}Prot\'s House.jpg'.format(ppath)))
    thfsc5_pic1 = tk.Label(thfsc5, image = tbg1, bd=5)
    thfsc5_pic1.place(x = 0, y = 0, anchor = 'nw')

    tbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 1.jpg'.format(tpath)))
    thfsc5_pic2 = tk.Label(thfsc5, image = tbg2, bd=5)
    thfsc5_pic2.place(x = 1320, y = 0, anchor = 'nw')

    thfsc5_fr1 = tk.Frame(thfsc5, width = 555, height = 365, bg = 'red')
    thfsc5_fr1.place(x = 15, y = 700, anchor = 'nw')
    thfsc5_fr1.propagate(0)

    thfsc5_opt1 = tk.Button(thfsc5_fr1, text = 'Horse',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white',command=thfstr6)
    thfsc5_opt1.pack(fill = 'both', expand = True)

    thfsc5_fr2 = tk.Frame(thfsc5, width = 555, height = 365, bg = 'blue')
    thfsc5_fr2.place(x = 575, y = 700, anchor = 'nw')
    thfsc5_fr2.propagate(0)

    thfsc5_opt2 = tk.Button(thfsc5_fr2, text = 'On \nFoot',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white',command=thfstr7)
    thfsc5_opt2.pack(fill = 'both', expand = True)

    thfsc5_fr3 = tk.Frame(thfsc5, width = 550, height = 363, bg = 'green')
    thfsc5_fr3.place(x = 1135, y = 700, anchor = 'nw')
    thfsc5_fr3.propagate(0)

    thfsc5_opt3 = tk.Button(thfsc5_fr3, text = 'Use a Witch\'s\nTeleportation\nPotion',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white',command=thfstr8)
    thfsc5_opt3.pack(fill = 'both', expand = True)

    thfsc5_pla = tk.Button(thfsc5, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc5_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc5_pau = tk.Button(thfsc5, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc5_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc5_fr4 = tk.Frame(thfsc5, width = 125, height = 105, bg = 'red')
    thfsc5_fr4.place(x = 1790, y = 690, anchor = 'nw')
    thfsc5_fr4.propagate(0)

    thfsc5_heli = tk.Label(thfsc5, image = health_icn, bd = 0, bg = 'white')
    thfsc5_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    thfsc5_helt = tk.Label(thfsc5_fr4, text = health2[0], font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc5_helt.pack(fill = 'both', expand = True)

    thfsc5_fr5 = tk.Frame(thfsc5, width = 125, height = 105, bg = 'red')
    thfsc5_fr5.place(x = 1790, y = 790, anchor = 'nw')
    thfsc5_fr5.propagate(0)

    thfsc5_armi = tk.Label(thfsc5, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    thfsc5_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    thfsc5_armt = tk.Label(thfsc5_fr5, text = armour2[0], font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc5_armt.pack(fill = 'both', expand = True)

    thfsc5_inv = tk.Button(thfsc5, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    thfsc5_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc5_ext = tk.Button(thfsc5, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    thfsc5_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc5";')
    con.commit()

    thfsc5.mainloop()


def thfstr6():
    
    global thfsc6

    try:
        thfsc5.after(500, lambda: thfsc5.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc6 = tk.Toplevel()
    thfsc6.attributes('-fullscreen', True)
    thfsc6.configure(bd = 1)

    thfsc6_can = tk.Canvas(thfsc6, width = 1920, height = 1080, bg = 'black')
    thfsc6_can.pack(expand = True, fill = 'both')

    thfsc6_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    tbg1 = ImageTk.PhotoImage(Image.open('{}Ogre in a Jungle.jpg'.format(ppath)))
    thfsc6_pic1 = tk.Label(thfsc6, image = tbg1, bd=5)
    thfsc6_pic1.place(x = 0, y = 0, anchor = 'nw')

    tbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 2.jpg'.format(tpath)))
    thfsc6_pic2 = tk.Label(thfsc6, image = tbg2, bd=5)
    thfsc6_pic2.place(x = 1320, y = 0, anchor = 'nw')

    thfsc6_fr1 = tk.Frame(thfsc6, width = 555, height = 365, bg = 'red')
    thfsc6_fr1.place(x = 15, y = 700, anchor = 'nw')
    thfsc6_fr1.propagate(0)

    thfsc6_opt1 = tk.Button(thfsc6_fr1, font = ('Enchanted Land', 80),
                        text = 'Signal Your\nHorse to Leave',                            
                        bg = '#090D3A', fg = 'white', command = thfstr9)
    thfsc6_opt1.pack(fill = 'both', expand = True)

    thfsc6_fr2 = tk.Frame(thfsc6, width = 555, height = 365, bg = 'blue')
    thfsc6_fr2.place(x = 575, y = 700, anchor = 'nw')
    thfsc6_fr2.propagate(0)

    thfsc6_opt2 = tk.Button(thfsc6_fr2, font = ('Enchanted Land', 80),
                            text = 'Get off Your\n Horse Without Silently',                            
                            bg = '#090D3A', fg = 'white', command = thfstr10)
    thfsc6_opt2.pack(fill = 'both', expand = True)

    thfsc6_fr3 = tk.Frame(thfsc6, width = 550, height = 363, bg = 'green')
    thfsc6_fr3.place(x = 1135, y = 700, anchor = 'nw')
    thfsc6_fr3.propagate(0)

    thfsc6_opt3 = tk.Button(thfsc6_fr3, text = 'Attempt to Fight\n the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr11)
    thfsc6_opt3.pack(fill = 'both', expand = True)

    thfsc6_pla = tk.Button(thfsc6, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc6_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc6_pau = tk.Button(thfsc6, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc6_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc6_heli = tk.Label(thfsc6, image = health_icn, bd = 0, bg = 'white')
    thfsc6_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    thfsc6_helt = tk.Label(thfsc6, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc6_helt.place(x = 1916, y = 690, anchor = 'ne')

    thfsc6_armi = tk.Label(thfsc6, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    thfsc6_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    thfsc6_armt = tk.Label(thfsc6, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc6_armt.place(x = 1916, y = 790, anchor = 'ne')

    thfsc6_inv = tk.Button(thfsc6, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    thfsc6_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc6_ext = tk.Button(thfsc6, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    thfsc6_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc6";')
    con.commit()

    thfsc6.mainloop()



def thfstr7():
    
    global thfsc7

    try:
        thfsc5.after(500, lambda: thfsc5.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass
    
    thfsc7 = tk.Toplevel()
    thfsc7.attributes('-fullscreen', True)
    thfsc7.configure(bd = 1)

    thfsc7_can = tk.Canvas(thfsc7, width = 1920, height = 1080, bg = 'black')
    thfsc7_can.pack(expand = True, fill = 'both')

    thfsc7_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    tbg1 = ImageTk.PhotoImage(Image.open('{}Ogre in a Jungle.jpg'.format(ppath)))
    thfsc7_pic1 = tk.Label(thfsc7, image = tbg1, bd=5)
    thfsc7_pic1.place(x = 0, y = 0, anchor = 'nw')

    tbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 3.jpg'.format(tpath)))
    thfsc7_pic2 = tk.Label(thfsc7, image = tbg2, bd=5)
    thfsc7_pic2.place(x = 1320, y = 0, anchor = 'nw')

    thfsc7_fr1 = tk.Frame(thfsc7, width = 555, height = 365, bg = 'red')
    thfsc7_fr1.place(x = 15, y = 700, anchor = 'nw')
    thfsc7_fr1.propagate(0)

    thfsc7_opt1 = tk.Button(thfsc7_fr1, text = 'Attempt to\n Distract the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr12)
    thfsc7_opt1.pack(fill = 'both', expand = True)

    thfsc7_fr2 = tk.Frame(thfsc7, width = 555, height = 365, bg = 'blue')
    thfsc7_fr2.place(x = 575, y = 700, anchor = 'nw')
    thfsc7_fr2.propagate(0)

    thfsc7_opt2 = tk.Button(thfsc7_fr2, text = 'Attempt to\n Fight the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr11)
    thfsc7_opt2.pack(fill = 'both', expand = True)

    thfsc7_fr3 = tk.Frame(thfsc7, width = 550, height = 363, bg = 'green')
    thfsc7_fr3.place(x = 1135, y = 700, anchor = 'nw')
    thfsc7_fr3.propagate(0)

    thfsc7_opt3 = tk.Button(thfsc7_fr3, text = 'Hide and Hope\n that the Ogre\n Goes Away',
                        font = ('Enchanted Land', 80),
                        bg = '#090D3A', fg = 'white', command = thfstr13)
    thfsc7_opt3.pack(fill = 'both', expand = True)

    thfsc7_pla = tk.Button(thfsc7, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc7_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc7_pau = tk.Button(thfsc7, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc7_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc7_heli = tk.Label(thfsc7, image = health_icn, bd = 0, bg = 'white')
    thfsc7_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    thfsc7_helt = tk.Label(thfsc7, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc7_helt.place(x = 1916, y = 690, anchor = 'ne')

    thfsc7_armi = tk.Label(thfsc7, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    thfsc7_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    thfsc7_armt = tk.Label(thfsc7, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc7_armt.place(x = 1916, y = 790, anchor = 'ne')

    thfsc7_inv = tk.Button(thfsc7, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    thfsc7_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc7_ext = tk.Button(thfsc7, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    thfsc7_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc7";')
    con.commit()

    thfsc7.mainloop()



def thfstr8():
    
    global thfsc8

    try:
        thfsc5.after(500, lambda: thfsc5.destroy())
    except NameError:
        pass

    try:
        thfsc11.after(500, lambda: thfsc11.destroy())
    except NameError:
        pass

    try:
        thfsc12.after(500, lambda: thfsc12.destroy())
    except NameError:
        pass

    try:
        thfsc13.after(500, lambda: thfsc13.destroy())
    except NameError:
        pass

    try:
        thfsc14.after(500, lambda: thfsc14.destroy())
    except NameError:
        pass

    try:
        thfsc15.after(500, lambda: thfsc15.destroy())
    except NameError:
        pass

    try:
        thfsc17.after(500, lambda: thfsc17.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc8 = tk.Toplevel()
    thfsc8.attributes('-fullscreen', True)
    thfsc8.configure(bd = 0)

    thfsc8_can = tk.Canvas(thfsc8, width = 1920, height = 1080, bg = 'black')
    thfsc8_can.pack(expand = True, fill = 'both')
    
    tbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 5.jpg'.format(tpath)))
    thfsc8_can.create_image(0, 0, image = tbg1, anchor = 'nw')

    thfsc8_pla = tk.Button(thfsc8, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc8_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc8_pau = tk.Button(thfsc8, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc8_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc8_ext = tk.Button(thfsc8, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    thfsc8_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc8";')
    con.commit()

    thfsc8.mainloop()



def thfstr9():
    
    global thfsc9

    try:
        thfsc6.after(500, lambda: thfsc6.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc9 = tk.Toplevel()
    thfsc9.attributes('-fullscreen', True)
    thfsc9.configure(bd = 1)

    thfsc9_can = tk.Canvas(thfsc9, width = 1920, height = 1080, bg = 'black')
    thfsc9_can.pack(expand = True, fill = 'both')

    thfsc9_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    tbg1 = ImageTk.PhotoImage(Image.open('{}Horsecart 1.jpg'.format(ppath)))
    thfsc9_pic1 = tk.Label(thfsc9, image = tbg1, bd=5)
    thfsc9_pic1.place(x = 0, y = 0, anchor = 'nw')

    tbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 4.jpg'.format(tpath)))
    thfsc9_pic2 = tk.Label(thfsc9, image = tbg2, bd=5)
    thfsc9_pic2.place(x = 1320, y = 0, anchor = 'nw')

    thfsc9_fr1 = tk.Frame(thfsc9, width = 555, height = 365, bg = 'red')
    thfsc9_fr1.place(x = 15, y = 700, anchor = 'nw')
    thfsc9_fr1.propagate(0)

    thfsc9_opt1 = tk.Button(thfsc9_fr1, text = 'Attempt to\n Distract the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr12)
    thfsc9_opt1.pack(fill = 'both', expand = True)

    thfsc9_fr2 = tk.Frame(thfsc9, width = 555, height = 365, bg = 'blue')
    thfsc9_fr2.place(x = 575, y = 700, anchor = 'nw')
    thfsc9_fr2.propagate(0)

    thfsc9_opt2 = tk.Button(thfsc9_fr2, text = 'Attempt to\n Fight the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr11)
    thfsc9_opt2.pack(fill = 'both', expand = True)

    thfsc9_fr3 = tk.Frame(thfsc9, width = 550, height = 363, bg = 'green')
    thfsc9_fr3.place(x = 1135, y = 700, anchor = 'nw')
    thfsc9_fr3.propagate(0)

    thfsc9_opt3 = tk.Button(thfsc9_fr3, text = 'Hide and Hope\nthat the Ogre\nGoes Away',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr13)
    thfsc9_opt3.pack(fill = 'both', expand = True)

    thfsc9_pla = tk.Button(thfsc9, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc9_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc9_pau = tk.Button(thfsc9, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc9_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc9_heli = tk.Label(thfsc9, image = health_icn, bd = 0, bg = 'white')
    thfsc9_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    thfsc9_helt = tk.Label(thfsc9, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc9_helt.place(x = 1916, y = 690, anchor = 'ne')

    thfsc9_armi = tk.Label(thfsc9, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    thfsc9_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    thfsc9_armt = tk.Label(thfsc9, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc9_armt.place(x = 1916, y = 790, anchor = 'ne')

    thfsc9_inv = tk.Button(thfsc9, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    thfsc9_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc9_ext = tk.Button(thfsc9, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    thfsc9_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc9";')
    con.commit()

    thfsc9.mainloop()



def thfstr10():
    
    global thfsc10

    try:
        thfsc6.after(500, lambda: thfsc6.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc10 = tk.Toplevel()
    thfsc10.attributes('-fullscreen', True)
    thfsc10.configure(bd = 1)

    thfsc10_can = tk.Canvas(thfsc10, width = 1920, height = 1080, bg = 'black')
    thfsc10_can.pack(expand = True, fill = 'both')

    thfsc10_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    tbg1 = ImageTk.PhotoImage(Image.open('{}Wagon.jpg'.format(ppath)))
    thfsc10_pic1 = tk.Label(thfsc10, image = tbg1, bd=5)
    thfsc10_pic1.place(x = 0, y = 0, anchor = 'nw')

    tbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 5.jpg'.format(tpath)))
    thfsc10_pic2 = tk.Label(thfsc10, image = tbg2, bd=5)
    thfsc10_pic2.place(x = 1320, y = 0, anchor = 'nw')

    thfsc10_fr1 = tk.Frame(thfsc10, width = 555, height = 365, bg = 'red')
    thfsc10_fr1.place(x = 15, y = 700, anchor = 'nw')
    thfsc10_fr1.propagate(0)

    thfsc10_opt1 = tk.Button(thfsc10_fr1, text = 'Attempt to\n Distract the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr12)
    thfsc10_opt1.pack(fill = 'both', expand = True)

    thfsc10_fr2 = tk.Frame(thfsc10, width = 555, height = 365, bg = 'blue')
    thfsc10_fr2.place(x = 575, y = 700, anchor = 'nw')
    thfsc10_fr2.propagate(0)

    thfsc10_opt2 = tk.Button(thfsc10_fr2, text = 'Attempt to\n Fight the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr11)
    thfsc10_opt2.pack(fill = 'both', expand = True)

    thfsc10_fr3 = tk.Frame(thfsc10, width = 550, height = 363, bg = 'green')
    thfsc10_fr3.place(x = 1135, y = 700, anchor = 'nw')
    thfsc10_fr3.propagate(0)

    thfsc10_opt3 = tk.Button(thfsc10_fr3, text = 'Hide and Hope\n that the Ogre\n Goes Away',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr13)
    thfsc10_opt3.pack(fill = 'both', expand = True)

    thfsc10_pla = tk.Button(thfsc10, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc10_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc10_pau = tk.Button(thfsc10, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc10_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc10_heli = tk.Label(thfsc10, image = health_icn, bd = 0, bg = 'white')
    thfsc10_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    thfsc10_helt = tk.Label(thfsc10, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc10_helt.place(x = 1916, y = 690, anchor = 'ne')

    thfsc10_armi = tk.Label(thfsc10, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    thfsc10_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    thfsc10_armt = tk.Label(thfsc10, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc10_armt.place(x = 1916, y = 790, anchor = 'ne')

    thfsc10_inv = tk.Button(thfsc10, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    thfsc10_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc10_ext = tk.Button(thfsc10, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    thfsc10_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc10";')
    con.commit()

    thfsc10.mainloop()



def thfstr11():
    
    global thfsc11

    try:
        thfsc6.after(500, lambda: thfsc6.destroy())
    except NameError:
        pass

    try:
        thfsc7.after(500, lambda: thfsc7.destroy())
    except NameError:
        pass

    try:
        thfsc9.after(500, lambda: thfsc9.destroy())
    except NameError:
        pass

    try:
        thfsc10.after(500, lambda: thfsc10.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc11 = tk.Toplevel()
    thfsc11.attributes('-fullscreen', True)
    thfsc11.configure(bd = 1)

    thfsc11_can = tk.Canvas(thfsc11, width = 1920, height = 1080, bg = 'black')
    thfsc11_can.pack(expand = True, fill = 'both')

    thfsc11_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    tbg1 = ImageTk.PhotoImage(Image.open('{}Ogre Fight.jpg'.format(ppath)))
    thfsc11_pic1 = tk.Label(thfsc11, image = tbg1, bd=5)
    thfsc11_pic1.place(x = 0, y = 0, anchor = 'nw')

    tbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 6.jpg'.format(tpath)))
    thfsc11_pic2 = tk.Label(thfsc11, image = tbg2, bd=5)
    thfsc11_pic2.place(x = 1320, y = 0, anchor = 'nw')

    thfsc11_fr1 = tk.Frame(thfsc11, width = 555, height = 365, bg = 'red')
    thfsc11_fr1.place(x = 15, y = 700, anchor = 'nw')
    thfsc11_fr1.propagate(0)

    thfsc11_opt1 = tk.Button(thfsc11_fr1, text = 'Poison\nthe Ogre using a\nPoisoned Blade',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = thfstr14)
    thfsc11_opt1.pack(fill = 'both', expand = True)

    thfsc11_fr2 = tk.Frame(thfsc11, width = 555, height = 365, bg = 'blue')
    thfsc11_fr2.place(x = 575, y = 700, anchor = 'nw')
    thfsc11_fr2.propagate(0)

    thfsc11_opt2 = tk.Button(thfsc11_fr2, text = 'Tie Up\nthe Ogre\nUsing Chains',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = thfstr15)
    thfsc11_opt2.pack(fill = 'both', expand = True)

    thfsc11_fr3 = tk.Frame(thfsc11, width = 550, height = 363, bg = 'green')
    thfsc11_fr3.place(x = 1135, y = 700, anchor = 'nw')
    thfsc11_fr3.propagate(0)

    thfsc11_opt3 = tk.Button(thfsc11_fr3, text = 'Use Your Knife\n to Attack',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr8)
    thfsc11_opt3.pack(fill = 'both', expand = True)

    thfsc11_pla = tk.Button(thfsc11, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc11_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc11_pau = tk.Button(thfsc11, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc11_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc11_heli = tk.Label(thfsc11, image = health_icn, bd = 0, bg = 'white')
    thfsc11_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    thfsc11_helt = tk.Label(thfsc11, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc11_helt.place(x = 1916, y = 690, anchor = 'ne')

    thfsc11_armi = tk.Label(thfsc11, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    thfsc11_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    thfsc11_armt = tk.Label(thfsc11, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc11_armt.place(x = 1916, y = 790, anchor = 'ne')

    thfsc11_inv = tk.Button(thfsc11, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    thfsc11_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc11_ext = tk.Button(thfsc11, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    thfsc11_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc11";')
    con.commit()

    thfsc11.mainloop()



def thfstr12():
    
    global thfsc12

    try:
        thfsc7.after(500, lambda: thfsc7.destroy())
    except NameError:
        pass

    try:
        thfsc9.after(500, lambda: thfsc9.destroy())
    except NameError:
        pass

    try:
        thfsc10.after(500, lambda: thfsc10.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc12 = tk.Toplevel()
    thfsc12.attributes('-fullscreen', True)
    thfsc12.configure(bd = 1)

    thfsc12_can = tk.Canvas(thfsc12, width = 1920, height = 1080, bg = 'black')
    thfsc12_can.pack(expand = True, fill = 'both')

    thfsc12_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    tbg1 = ImageTk.PhotoImage(Image.open('{}Wizard Story.jpg'.format(ppath)))
    thfsc12_pic1 = tk.Label(thfsc12, image = tbg1, bd=5)
    thfsc12_pic1.place(x = 0, y = 0, anchor = 'nw')

    tbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 7.jpg'.format(tpath)))
    thfsc12_pic2 = tk.Label(thfsc12, image = tbg2, bd=5)
    thfsc12_pic2.place(x = 1320, y = 0, anchor = 'nw')

    thfsc12_fr1 = tk.Frame(thfsc12, width = 555, height = 365, bg = 'red')
    thfsc12_fr1.place(x = 15, y = 700, anchor = 'nw')
    thfsc12_fr1.propagate(0)

    thfsc12_opt1 = tk.Button(thfsc12_fr1, font = ('Enchanted Land', 55),
                             text = 'Use a Bomb\n to Make an\nExplosion and Run',
                             bg = '#090D3A', fg = 'white', command = thfstr16)
    thfsc12_opt1.pack(fill = 'both', expand = True)

    thfsc12_fr2 = tk.Frame(thfsc12, width = 555, height = 365, bg = 'blue')
    thfsc12_fr2.place(x = 575, y = 700, anchor = 'nw')
    thfsc12_fr2.propagate(0)

    thfsc12_opt2 = tk.Button(thfsc12_fr2, text = 'Use a\nSmokebomb',
                            font = ('Enchanted Land', 70),
                            bg = '#090D3A', fg = 'white', command = thfstr17)
    thfsc12_opt2.pack(fill = 'both', expand = True)

    thfsc12_fr3 = tk.Frame(thfsc12, width = 550, height = 363, bg = 'green')
    thfsc12_fr3.place(x = 1135, y = 700, anchor = 'nw')
    thfsc12_fr3.propagate(0)

    thfsc12_opt3 = tk.Button(thfsc12_fr3, text = 'Throw a Big Rock\n in the Lake Nearby',
                            font = ('Enchanted Land', 75),
                            bg = '#090D3A', fg = 'white', command = thfstr8)
    thfsc12_opt3.pack(fill = 'both', expand = True)

    thfsc12_pla = tk.Button(thfsc12, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc12_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc12_pau = tk.Button(thfsc12, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc12_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc12_heli = tk.Label(thfsc12, image = health_icn, bd = 0, bg = 'white')
    thfsc12_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    thfsc12_helt = tk.Label(thfsc12, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc12_helt.place(x = 1916, y = 690, anchor = 'ne')

    thfsc12_armi = tk.Label(thfsc12, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    thfsc12_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    thfsc12_armt = tk.Label(thfsc12, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc12_armt.place(x = 1916, y = 790, anchor = 'ne')

    thfsc12_inv = tk.Button(thfsc12, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    thfsc12_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc12_ext = tk.Button(thfsc12, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    thfsc12_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc12";')
    con.commit()

    thfsc12.mainloop()




def thfstr13():
    
    global thfsc13

    try:
        thfsc7.after(500, lambda: thfsc7.destroy())
    except NameError:
        pass

    try:
        thfsc9.after(500, lambda: thfsc9.destroy())
    except NameError:
        pass

    try:
        thfsc10.after(500, lambda: thfsc10.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc13 = tk.Toplevel()
    thfsc13.attributes('-fullscreen', True)
    thfsc13.configure(bd = 1)

    thfsc13_can = tk.Canvas(thfsc13, width = 1920, height = 1080, bg = 'black')
    thfsc13_can.pack(expand = True, fill = 'both')

    thfsc13_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    tbg1 = ImageTk.PhotoImage(Image.open('{}Ogre Fight.jpg'.format(ppath)))
    thfsc13_pic1 = tk.Label(thfsc13, image = tbg1, bd=5)
    thfsc13_pic1.place(x = 0, y = 0, anchor = 'nw')

    tbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 8.jpg'.format(tpath)))
    thfsc13_pic2 = tk.Label(thfsc13, image = tbg2, bd=5)
    thfsc13_pic2.place(x = 1320, y = 0, anchor = 'nw')

    thfsc13_fr1 = tk.Frame(thfsc13, width = 555, height = 365, bg = 'red')
    thfsc13_fr1.place(x = 15, y = 700, anchor = 'nw')
    thfsc13_fr1.propagate(0)

    thfsc13_opt1 = tk.Button(thfsc13_fr1, text = 'Poison\nthe Ogre using a\nPoisoned Blade',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = thfstr14)
    thfsc13_opt1.pack(fill = 'both', expand = True)

    thfsc13_fr2 = tk.Frame(thfsc13, width = 555, height = 365, bg = 'blue')
    thfsc13_fr2.place(x = 575, y = 700, anchor = 'nw')
    thfsc13_fr2.propagate(0)

    thfsc13_opt2 = tk.Button(thfsc13_fr2, text = 'Tie Up\nthe Ogre\nUsing Chains',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = thfstr15)
    thfsc13_opt2.pack(fill = 'both', expand = True)

    thfsc13_fr3 = tk.Frame(thfsc13, width = 550, height = 363, bg = 'green')
    thfsc13_fr3.place(x = 1135, y = 700, anchor = 'nw')
    thfsc13_fr3.propagate(0)

    thfsc13_opt3 = tk.Button(thfsc13_fr3, text = 'Try to Stab\n the Ogre with\n Your Knife',
                            font = ('Enchanted Land', 70),
                            bg = '#090D3A', fg = 'white', command = thfstr8)
    thfsc13_opt3.pack(fill = 'both', expand = True)

    thfsc13_pla = tk.Button(thfsc13, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc13_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc13_pau = tk.Button(thfsc13, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc13_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc13_heli = tk.Label(thfsc13, image = health_icn, bd = 0, bg = 'white')
    thfsc13_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    thfsc13_helt = tk.Label(thfsc13, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc13_helt.place(x = 1916, y = 690, anchor = 'ne')

    thfsc13_armi = tk.Label(thfsc13, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    thfsc13_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    thfsc13_armt = tk.Label(thfsc13, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc13_armt.place(x = 1916, y = 790, anchor = 'ne')

    thfsc13_inv = tk.Button(thfsc13, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    thfsc13_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc13_ext = tk.Button(thfsc13, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    thfsc13_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc13";')
    con.commit()

    thfsc13.mainloop()



def thfstr14():
    
    global thfsc14

    try:
        thfsc11.after(500, lambda: thfsc11.destroy())
    except NameError:
        pass

    try:
        thfsc13.after(500, lambda: thfsc13.destroy())
    except NameError:
        pass

    try:
        thfsc17.after(500, lambda: thfsc17.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc14 = tk.Toplevel()
    thfsc14.attributes('-fullscreen', True)
    thfsc14.configure(bd = 1)

    thfsc14_can = tk.Canvas(thfsc14, width = 1920, height = 1080, bg = 'black')
    thfsc14_can.pack(expand = True, fill = 'both')
    
    thfsc14_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    tbg1 = ImageTk.PhotoImage(Image.open('{}Poison.jpg'.format(ppath)))
    thfsc14_pic1 = tk.Label(thfsc14, image = tbg1, bd=5)
    thfsc14_pic1.place(x = 0, y = 0, anchor = 'nw')

    tbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 9.jpg'.format(tpath)))
    thfsc14_pic2 = tk.Label(thfsc14, image = tbg2, bd=5)
    thfsc14_pic2.place(x = 1320, y = 0, anchor = 'nw')

    thfsc14_fr1 = tk.Frame(thfsc14, width = 555, height = 365, bg = 'red')
    thfsc14_fr1.place(x = 15, y = 700, anchor = 'nw')
    thfsc14_fr1.propagate(0)

    thfsc14_opt1 = tk.Button(thfsc14_fr1, text = 'Knock it\nUnconcious\n with your Dagger\'s Hilt',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr16)
    thfsc14_opt1.pack(fill = 'both', expand = True)

    thfsc14_fr2 = tk.Frame(thfsc14, width = 555, height = 365, bg = 'blue')
    thfsc14_fr2.place(x = 575, y = 700, anchor = 'nw')
    thfsc14_fr2.propagate(0)

    thfsc14_opt2 = tk.Button(thfsc14_fr2, text = 'Use Your Knife to\nPut an End to\n the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr16)
    thfsc14_opt2.pack(fill = 'both', expand = True)

    thfsc14_fr3 = tk.Frame(thfsc14, width = 550, height = 363, bg = 'green')
    thfsc14_fr3.place(x = 1135, y = 700, anchor = 'nw')
    thfsc14_fr3.propagate(0)

    thfsc14_opt3 = tk.Button(thfsc14_fr3, text = 'Leave the Ogre\n and Let Time Put\n an End to it',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr8)
    thfsc14_opt3.pack(fill = 'both', expand = True)

    thfsc14_pla = tk.Button(thfsc14, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc14_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc14_pau = tk.Button(thfsc14, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc14_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc14_heli = tk.Label(thfsc14, image = health_icn, bd = 0, bg = 'white')
    thfsc14_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    thfsc14_helt = tk.Label(thfsc14, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc14_helt.place(x = 1916, y = 690, anchor = 'ne')

    thfsc14_armi = tk.Label(thfsc14, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    thfsc14_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    thfsc14_armt = tk.Label(thfsc14, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc14_armt.place(x = 1916, y = 790, anchor = 'ne')

    thfsc14_inv = tk.Button(thfsc14, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    thfsc14_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc14_ext = tk.Button(thfsc14, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    thfsc14_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc14";')
    con.commit()

    thfsc14.mainloop()



def thfstr15():
    
    global thfsc15

    try:
        thfsc11.after(500, lambda: thfsc11.destroy())
    except NameError:
        pass

    try:
        thfsc13.after(500, lambda: thfsc13.destroy())
    except NameError:
        pass

    try:
        thfsc17.after(500, lambda: thfsc17.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc15 = tk.Toplevel()
    thfsc15.attributes('-fullscreen', True)
    thfsc15.configure(bd = 1)

    thfsc15_can = tk.Canvas(thfsc15, width = 1920, height = 1080, bg = 'black')
    thfsc15_can.pack(expand = True, fill = 'both')
    
    thfsc15_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    tbg1 = ImageTk.PhotoImage(Image.open('{}Chains.jpg'.format(ppath)))
    thfsc15_pic1 = tk.Label(thfsc15, image = tbg1, bd=5)
    thfsc15_pic1.place(x = 0, y = 0, anchor = 'nw')

    tbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 10.jpg'.format(tpath)))
    thfsc15_pic2 = tk.Label(thfsc15, image = tbg2, bd=5)
    thfsc15_pic2.place(x = 1320, y = 0, anchor = 'nw')

    thfsc15_fr1 = tk.Frame(thfsc15, width = 555, height = 365, bg = 'red')
    thfsc15_fr1.place(x = 15, y = 700, anchor = 'nw')
    thfsc15_fr1.propagate(0)

    thfsc15_opt1 = tk.Button(thfsc15_fr1, text = 'Knock it\nUnconcious\n with your Dagger\'s Hilt',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr16)
    thfsc15_opt1.pack(fill = 'both', expand = True)

    thfsc15_fr2 = tk.Frame(thfsc15, width = 555, height = 365, bg = 'blue')
    thfsc15_fr2.place(x = 575, y = 700, anchor = 'nw')
    thfsc15_fr2.propagate(0)

    thfsc15_opt2 = tk.Button(thfsc15_fr2, text = 'Use Your Knife\nto Put an End\nto the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr16)
    thfsc15_opt2.pack(fill = 'both', expand = True)

    thfsc15_fr3 = tk.Frame(thfsc15, width = 550, height = 363, bg = 'green')
    thfsc15_fr3.place(x = 1135, y = 700, anchor = 'nw')
    thfsc15_fr3.propagate(0)

    thfsc15_opt3 = tk.Button(thfsc15_fr3, text = 'Make a\nRun for it',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = thfstr8)
    thfsc15_opt3.pack(fill = 'both', expand = True)

    thfsc15_pla = tk.Button(thfsc15, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc15_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc15_pau = tk.Button(thfsc15, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc15_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc15_heli = tk.Label(thfsc15, image = health_icn, bd = 0, bg = 'white')
    thfsc15_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    thfsc15_helt = tk.Label(thfsc15, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc15_helt.place(x = 1916, y = 690, anchor = 'ne')

    thfsc15_armi = tk.Label(thfsc15, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    thfsc15_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    thfsc15_armt = tk.Label(thfsc15, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc15_armt.place(x = 1916, y = 790, anchor = 'ne')

    thfsc15_inv = tk.Button(thfsc15, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    thfsc15_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc15_ext = tk.Button(thfsc15, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    thfsc15_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc15";')
    con.commit()

    thfsc15.mainloop()



def thfstr16():

    global thfsc16

    try:
        thfsc12.after(500, lambda: thfsc12.destroy())
    except NameError:
        pass

    try:
        thfsc14.after(500, lambda: thfsc14.destroy())
    except NameError:
        pass

    try:
        thfsc15.after(500, lambda: thfsc15.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc16 = tk.Toplevel()
    thfsc16.attributes('-fullscreen', True)
    thfsc16.configure(bd = 0)

    thfsc16_can = tk.Canvas(thfsc16, width = 1920, height = 1080, bg = 'black')
    thfsc16_can.pack(expand = True, fill = 'both')
    
    tbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 6.jpg'.format(tpath)))
    thfsc16_can.create_image(0, 0, image = tbg1, anchor = 'nw')

    thfsc16_pla = tk.Button(thfsc16, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc16_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc16_pau = tk.Button(thfsc16, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc16_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc16_inv = tk.Button(thfsc16, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7)
    thfsc16_inv.place(x = 1916, y = 890, anchor = 'ne')

    thfsc16_ext = tk.Button(thfsc16,text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    thfsc16_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc16";')
    con.commit()

    thfsc16.mainloop()



def thfstr17():
    
    global thfsc17

    try:
        thfsc12.after(500, lambda: thfsc12.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    thfsc17 = tk.Toplevel()
    thfsc17.attributes('-fullscreen', True)
    thfsc17.configure(bd = 1)

    thfsc17_can = tk.Canvas(thfsc17, width = 1920, height = 1080, bg = 'black')
    thfsc17_can.pack(expand = True, fill = 'both')
    
    thfsc17_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    tbg1 = ImageTk.PhotoImage(Image.open('{}Smoke.jpg'.format(ppath)))
    thfsc17_pic1 = tk.Label(thfsc17, image = tbg1, bd=5)
    thfsc17_pic1.place(x = 0, y = 0, anchor = 'nw')

    tbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 11.jpg'.format(tpath)))
    thfsc17_pic2 = tk.Label(thfsc17, image = tbg2, bd=5)
    thfsc17_pic2.place(x = 1320, y = 0, anchor = 'nw')

    thfsc17_fr1 = tk.Frame(thfsc17, width = 555, height = 365, bg = 'red')
    thfsc17_fr1.place(x = 15, y = 700, anchor = 'nw')
    thfsc17_fr1.propagate(0)

    thfsc17_opt1 = tk.Button(thfsc17_fr1, text = 'Poison\nthe Ogre Using a\nPoisoned Blade',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = thfstr14)
    thfsc17_opt1.pack(fill = 'both', expand = True)

    thfsc17_fr2 = tk.Frame(thfsc17, width = 555, height = 365, bg = 'blue')
    thfsc17_fr2.place(x = 575, y = 700, anchor = 'nw')
    thfsc17_fr2.propagate(0)

    thfsc17_opt2 = tk.Button(thfsc17_fr2, text = 'Tie Up\nthe Ogre\nUsing Chains',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = thfstr15)
    thfsc17_opt2.pack(fill = 'both', expand = True)

    thfsc17_fr3 = tk.Frame(thfsc17, width = 550, height = 363, bg = 'green')
    thfsc17_fr3.place(x = 1135, y = 700, anchor = 'nw')
    thfsc17_fr3.propagate(0)

    thfsc17_opt3 = tk.Button(thfsc17_fr3, text = 'Attack the Ogre\n with Your Knife',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = thfstr8)
    thfsc17_opt3.pack(fill = 'both', expand = True)

    thfsc17_pla = tk.Button(thfsc17, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    thfsc17_pla.place(x = 1865, y = 5, anchor = 'ne')

    thfsc17_pau = tk.Button(thfsc17, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    thfsc17_pau.place(x = 1915, y = 5, anchor = 'ne')

    thfsc17_heli = tk.Label(thfsc17, image = health_icn, bd = 0, bg = 'white')
    thfsc17_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    thfsc17_helt = tk.Label(thfsc17, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc17_helt.place(x = 1916, y = 690, anchor = 'ne')

    thfsc17_armi = tk.Label(thfsc17, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    thfsc17_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    thfsc17_armt = tk.Label(thfsc17, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    thfsc17_armt.place(x = 1916, y = 790, anchor = 'ne')

    thfsc17_inv = tk.Button(thfsc17, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    thfsc17_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    thfsc17_ext = tk.Button(thfsc17, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    thfsc17_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "thfsc17";')
    con.commit()

    thfsc17.mainloop()


#########################################################################################


## Wizard's Story Begins ##

def wizstr1():
    
    global wizsc1

    try:
        chrsc.after(500, lambda: chrsc.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc1 = tk.Toplevel()
    wizsc1.attributes('-fullscreen', True)
    wizsc1.configure(bd = 0)

    wizsc1_can = tk.Canvas(wizsc1, width = 1920, height = 1080, bg = 'black')
    wizsc1_can.pack(expand = True, fill = 'both')
    
    wbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 1.jpg'.format(wpath)))
    wizsc1_can.create_image(0, 0, image = wbg1, anchor = 'nw')

    wizsc1_lbl = tk.Label(wizsc1, text = 'Welcome {}!'.format(save_name),
                   font = ('Enchanted Land', 100, 'bold'), padx = 20,
                   bg = '#0F0F0F', fg = 'white', relief = 'groove',)
    wizsc1_lbl.place(x = 960, y = 20, anchor = 'n')

    wizsc1_pla = tk.Button(wizsc1, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc1_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc1_pau = tk.Button(wizsc1, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc1_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc1_inv = tk.Button(wizsc1, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=wizstr2)
    wizsc1_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc1_ext = tk.Button(wizsc1, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    wizsc1_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc1";')
    con.commit()

    wizsc1.mainloop()

    
def wizstr2():
    
    global wizsc2

    try:
        wizsc1.after(500, lambda: wizsc1.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc2 = tk.Toplevel()
    wizsc2.attributes('-fullscreen', True)
    wizsc2.configure(bd = 0)

    wizsc2_can = tk.Canvas(wizsc2, width = 1920, height = 1080, bg = 'black')
    wizsc2_can.pack(expand = True, fill = 'both')
    
    wbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 2.jpg'.format(wpath)))
    wizsc2_can.create_image(0, 0, image = wbg1, anchor = 'nw')

    wizsc2_pla = tk.Button(wizsc2, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc2_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc2_pau = tk.Button(wizsc2, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc2_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc2_inv = tk.Button(wizsc2, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=wizstr3)
    wizsc2_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc2_ext = tk.Button(wizsc2, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    wizsc2_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc2";')
    con.commit()

    wizsc2.mainloop()


def wizstr3():
    
    global wizsc3

    try:
        wizsc2.after(500, lambda: wizsc2.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc3 = tk.Toplevel()
    wizsc3.attributes('-fullscreen', True)
    wizsc3.configure(bd = 0)

    wizsc3_can = tk.Canvas(wizsc3, width = 1920, height = 1080, bg = 'black')
    wizsc3_can.pack(expand = True, fill = 'both')
    
    wbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 3.jpg'.format(wpath)))
    wizsc3_can.create_image(0, 0, image = wbg1, anchor = 'nw')

    wizsc3_pla = tk.Button(wizsc3, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc3_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc3_pau = tk.Button(wizsc3, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc3_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc3_inv = tk.Button(wizsc3, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=wizstr4)
    wizsc3_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc3_ext = tk.Button(wizsc3, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    wizsc3_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc3";')
    con.commit()

    wizsc3.mainloop()


def wizstr4():
    
    global wizsc4

    try:
        wizsc3.after(500, lambda: wizsc3.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc4 = tk.Toplevel()
    wizsc4.attributes('-fullscreen', True)
    wizsc4.configure(bd = 0)

    wizsc4_can = tk.Canvas(wizsc4, width = 1920, height = 1080, bg = 'black')
    wizsc4_can.pack(expand = True, fill = 'both')
    
    wbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 4.jpg'.format(wpath)))
    wizsc4_can.create_image(0, 0, image = wbg1, anchor = 'nw')

    wizsc4_pla = tk.Button(wizsc4, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc4_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc4_pau = tk.Button(wizsc4, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc4_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc4_inv = tk.Button(wizsc4, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7,command=wizstr5)
    wizsc4_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc4_ext = tk.Button(wizsc4, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    wizsc4_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc4";')
    con.commit()

    cur.execute('insert into stats values (100, 000);')
    con.commit()

    cur.execute('insert into inventory (item_name, quantity) values ("Knife", 1)')
    con.commit()

    cur.execute('insert into inventory (item_name, quantity) values ("Leftover Bread", 1)')
    con.commit()

    cur.execute('insert into inventory (item_name, quantity) values ("Gold Coins", 100)')
    con.commit()

    wizsc4.mainloop()



def wizstr5():
    
    global wizsc5

    try:
        wizsc4.after(500, lambda: wizsc4.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    cur.execute('select health from stats;')
    health1 = cur.fetchall()
    health2 = health1[0]

    cur.execute('select armour from stats;')
    armour1 = cur.fetchall()
    armour2 = armour1[0]

    wizsc5 = tk.Toplevel()
    wizsc5.attributes('-fullscreen', True)
    wizsc5.configure(bd = 1)

    wizsc5_can = tk.Canvas(wizsc5, width = 1920, height = 1080, bg = 'black')
    wizsc5_can.pack(expand = True, fill = 'both')
    
    wizsc5_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    wbg1 = ImageTk.PhotoImage(Image.open('{}Prot\'s House.jpg'.format(ppath)))
    wizsc5_pic1 = tk.Label(wizsc5, image = wbg1, bd=5)
    wizsc5_pic1.place(x = 0, y = 0, anchor = 'nw')

    wbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 1.jpg'.format(wpath)))
    wizsc5_pic2 = tk.Label(wizsc5, image = wbg2, bd=5)
    wizsc5_pic2.place(x = 1320, y = 0, anchor = 'nw')

    wizsc5_fr1 = tk.Frame(wizsc5, width = 555, height = 365, bg = 'red')
    wizsc5_fr1.place(x = 15, y = 700, anchor = 'nw')
    wizsc5_fr1.propagate(0)

    wizsc5_opt1 = tk.Button(wizsc5_fr1, text = 'Horse \nCart',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white',command=wizstr6)
    wizsc5_opt1.pack(fill = 'both', expand = True)

    wizsc5_fr2 = tk.Frame(wizsc5, width = 555, height = 365, bg = 'blue')
    wizsc5_fr2.place(x = 575, y = 700, anchor = 'nw')
    wizsc5_fr2.propagate(0)

    wizsc5_opt2 = tk.Button(wizsc5_fr2, text = 'On \nFoot',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white',command=wizstr7)
    wizsc5_opt2.pack(fill = 'both', expand = True)

    wizsc5_fr3 = tk.Frame(wizsc5, width = 550, height = 363, bg = 'green')
    wizsc5_fr3.place(x = 1135, y = 700, anchor = 'nw')
    wizsc5_fr3.propagate(0)

    wizsc5_opt3 = tk.Button(wizsc5_fr3, text = 'Use a Vast\nTeleportation\nSpell',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white',command=wizstr8)
    wizsc5_opt3.pack(fill = 'both', expand = True)

    wizsc5_pla = tk.Button(wizsc5, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc5_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc5_pau = tk.Button(wizsc5, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc5_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc5_fr4 = tk.Frame(wizsc5, width = 125, height = 105, bg = 'red')
    wizsc5_fr4.place(x = 1790, y = 690, anchor = 'nw')
    wizsc5_fr4.propagate(0)

    wizsc5_heli = tk.Label(wizsc5, image = health_icn, bd = 0, bg = 'white')
    wizsc5_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    wizsc5_helt = tk.Label(wizsc5_fr4, text = health2[0], font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc5_helt.pack(fill = 'both', expand = True)

    wizsc5_fr5 = tk.Frame(wizsc5, width = 125, height = 105, bg = 'red')
    wizsc5_fr5.place(x = 1790, y = 790, anchor = 'nw')
    wizsc5_fr5.propagate(0)

    wizsc5_armi = tk.Label(wizsc5, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    wizsc5_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    wizsc5_armt = tk.Label(wizsc5_fr5, text = armour2[0], font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc5_armt.pack(fill = 'both', expand = True)

    wizsc5_inv = tk.Button(wizsc5, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    wizsc5_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc5_ext = tk.Button(wizsc5, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    wizsc5_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc5";')
    con.commit()

    wizsc5.mainloop()


def wizstr6():
    
    global wizsc6

    try:
        wizsc5.after(500, lambda: wizsc5.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc6 = tk.Toplevel()
    wizsc6.attributes('-fullscreen', True)
    wizsc6.configure(bd = 1)

    wizsc6_can = tk.Canvas(wizsc6, width = 1920, height = 1080, bg = 'black')
    wizsc6_can.pack(expand = True, fill = 'both')

    wizsc6_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    wbg1 = ImageTk.PhotoImage(Image.open('{}Ogre in a Jungle.jpg'.format(ppath)))
    wizsc6_pic1 = tk.Label(wizsc6, image = wbg1, bd=5)
    wizsc6_pic1.place(x = 0, y = 0, anchor = 'nw')

    wbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 2.jpg'.format(wpath)))
    wizsc6_pic2 = tk.Label(wizsc6, image = wbg2, bd=5)
    wizsc6_pic2.place(x = 1320, y = 0, anchor = 'nw')

    wizsc6_fr1 = tk.Frame(wizsc6, width = 555, height = 365, bg = 'red')
    wizsc6_fr1.place(x = 15, y = 700, anchor = 'nw')
    wizsc6_fr1.propagate(0)

    wizsc6_opt1 = tk.Button(wizsc6_fr1, font = ('Enchanted Land', 80),
                        text = 'Get off the Cart\n and Ask the \nRider to Leave',                            
                        bg = '#090D3A', fg = 'white', command = wizstr9)
    wizsc6_opt1.pack(fill = 'both', expand = True)

    wizsc6_fr2 = tk.Frame(wizsc6, width = 555, height = 365, bg = 'blue')
    wizsc6_fr2.place(x = 575, y = 700, anchor = 'nw')
    wizsc6_fr2.propagate(0)

    wizsc6_opt2 = tk.Button(wizsc6_fr2, font = ('Enchanted Land', 80),
                            text = 'Get off the Cart \nand Hide Without\n Alerting the Rider',                            
                            bg = '#090D3A', fg = 'white', command = wizstr10)
    wizsc6_opt2.pack(fill = 'both', expand = True)

    wizsc6_fr3 = tk.Frame(wizsc6, width = 550, height = 363, bg = 'green')
    wizsc6_fr3.place(x = 1135, y = 700, anchor = 'nw')
    wizsc6_fr3.propagate(0)

    wizsc6_opt3 = tk.Button(wizsc6_fr3, text = 'Attempt to Fight\n the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr11)
    wizsc6_opt3.pack(fill = 'both', expand = True)

    wizsc6_pla = tk.Button(wizsc6, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc6_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc6_pau = tk.Button(wizsc6, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc6_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc6_heli = tk.Label(wizsc6, image = health_icn, bd = 0, bg = 'white')
    wizsc6_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    wizsc6_helt = tk.Label(wizsc6, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc6_helt.place(x = 1916, y = 690, anchor = 'ne')

    wizsc6_armi = tk.Label(wizsc6, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    wizsc6_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    wizsc6_armt = tk.Label(wizsc6, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc6_armt.place(x = 1916, y = 790, anchor = 'ne')

    wizsc6_inv = tk.Button(wizsc6, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    wizsc6_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc6_ext = tk.Button(wizsc6, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    wizsc6_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc6";')
    con.commit()

    wizsc6.mainloop()



def wizstr7():
    
    global wizsc7

    try:
        wizsc5.after(500, lambda: wizsc5.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass
    
    wizsc7 = tk.Toplevel()
    wizsc7.attributes('-fullscreen', True)
    wizsc7.configure(bd = 1)

    wizsc7_can = tk.Canvas(wizsc7, width = 1920, height = 1080, bg = 'black')
    wizsc7_can.pack(expand = True, fill = 'both')

    wizsc7_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    wbg1 = ImageTk.PhotoImage(Image.open('{}Ogre in a Jungle.jpg'.format(ppath)))
    wizsc7_pic1 = tk.Label(wizsc7, image = wbg1, bd=5)
    wizsc7_pic1.place(x = 0, y = 0, anchor = 'nw')

    wbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 3.jpg'.format(wpath)))
    wizsc7_pic2 = tk.Label(wizsc7, image = wbg2, bd=5)
    wizsc7_pic2.place(x = 1320, y = 0, anchor = 'nw')

    wizsc7_fr1 = tk.Frame(wizsc7, width = 555, height = 365, bg = 'red')
    wizsc7_fr1.place(x = 15, y = 700, anchor = 'nw')
    wizsc7_fr1.propagate(0)

    wizsc7_opt1 = tk.Button(wizsc7_fr1, text = 'Attempt to\n Distract the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr12)
    wizsc7_opt1.pack(fill = 'both', expand = True)

    wizsc7_fr2 = tk.Frame(wizsc7, width = 555, height = 365, bg = 'blue')
    wizsc7_fr2.place(x = 575, y = 700, anchor = 'nw')
    wizsc7_fr2.propagate(0)

    wizsc7_opt2 = tk.Button(wizsc7_fr2, text = 'Attempt to\n Fight the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr11)
    wizsc7_opt2.pack(fill = 'both', expand = True)

    wizsc7_fr3 = tk.Frame(wizsc7, width = 550, height = 363, bg = 'green')
    wizsc7_fr3.place(x = 1135, y = 700, anchor = 'nw')
    wizsc7_fr3.propagate(0)

    wizsc7_opt3 = tk.Button(wizsc7_fr3, text = 'Hide and Hope\n that the Ogre\n Goes Away',
                        font = ('Enchanted Land', 80),
                        bg = '#090D3A', fg = 'white', command = wizstr13)
    wizsc7_opt3.pack(fill = 'both', expand = True)

    wizsc7_pla = tk.Button(wizsc7, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc7_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc7_pau = tk.Button(wizsc7, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc7_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc7_heli = tk.Label(wizsc7, image = health_icn, bd = 0, bg = 'white')
    wizsc7_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    wizsc7_helt = tk.Label(wizsc7, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc7_helt.place(x = 1916, y = 690, anchor = 'ne')

    wizsc7_armi = tk.Label(wizsc7, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    wizsc7_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    wizsc7_armt = tk.Label(wizsc7, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc7_armt.place(x = 1916, y = 790, anchor = 'ne')

    wizsc7_inv = tk.Button(wizsc7, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    wizsc7_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc7_ext = tk.Button(wizsc7, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    wizsc7_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc7";')
    con.commit()

    wizsc7.mainloop()



def wizstr8():
    
    global wizsc8

    try:
        wizsc5.after(500, lambda: wizsc5.destroy())
    except NameError:
        pass

    try:
        wizsc11.after(500, lambda: wizsc11.destroy())
    except NameError:
        pass

    try:
        wizsc12.after(500, lambda: wizsc12.destroy())
    except NameError:
        pass

    try:
        wizsc13.after(500, lambda: wizsc13.destroy())
    except NameError:
        pass

    try:
        wizsc14.after(500, lambda: wizsc14.destroy())
    except NameError:
        pass

    try:
        wizsc15.after(500, lambda: wizsc15.destroy())
    except NameError:
        pass

    try:
        wizsc17.after(500, lambda: wizsc17.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc8 = tk.Toplevel()
    wizsc8.attributes('-fullscreen', True)
    wizsc8.configure(bd = 0)

    wizsc8_can = tk.Canvas(wizsc8, width = 1920, height = 1080, bg = 'black')
    wizsc8_can.pack(expand = True, fill = 'both')
    
    wbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 5.jpg'.format(wpath)))
    wizsc8_can.create_image(0, 0, image = wbg1, anchor = 'nw')

    wizsc8_pla = tk.Button(wizsc8, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc8_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc8_pau = tk.Button(wizsc8, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc8_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc8_ext = tk.Button(wizsc8, text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    wizsc8_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc8";')
    con.commit()

    wizsc8.mainloop()



def wizstr9():
    
    global wizsc9

    try:
        wizsc6.after(500, lambda: wizsc6.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc9 = tk.Toplevel()
    wizsc9.attributes('-fullscreen', True)
    wizsc9.configure(bd = 1)

    wizsc9_can = tk.Canvas(wizsc9, width = 1920, height = 1080, bg = 'black')
    wizsc9_can.pack(expand = True, fill = 'both')

    wizsc9_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    wbg1 = ImageTk.PhotoImage(Image.open('{}Horsecart 1.jpg'.format(ppath)))
    wizsc9_pic1 = tk.Label(wizsc9, image = wbg1, bd=5)
    wizsc9_pic1.place(x = 0, y = 0, anchor = 'nw')

    wbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 4.jpg'.format(wpath)))
    wizsc9_pic2 = tk.Label(wizsc9, image = wbg2, bd=5)
    wizsc9_pic2.place(x = 1320, y = 0, anchor = 'nw')

    wizsc9_fr1 = tk.Frame(wizsc9, width = 555, height = 365, bg = 'red')
    wizsc9_fr1.place(x = 15, y = 700, anchor = 'nw')
    wizsc9_fr1.propagate(0)

    wizsc9_opt1 = tk.Button(wizsc9_fr1, text = 'Attempt to\n Distract the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr12)
    wizsc9_opt1.pack(fill = 'both', expand = True)

    wizsc9_fr2 = tk.Frame(wizsc9, width = 555, height = 365, bg = 'blue')
    wizsc9_fr2.place(x = 575, y = 700, anchor = 'nw')
    wizsc9_fr2.propagate(0)

    wizsc9_opt2 = tk.Button(wizsc9_fr2, text = 'Attempt to\n Fight the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr11)
    wizsc9_opt2.pack(fill = 'both', expand = True)

    wizsc9_fr3 = tk.Frame(wizsc9, width = 550, height = 363, bg = 'green')
    wizsc9_fr3.place(x = 1135, y = 700, anchor = 'nw')
    wizsc9_fr3.propagate(0)

    wizsc9_opt3 = tk.Button(wizsc9_fr3, text = 'Hide and Hope\nthat the Ogre\nGoes Away',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr13)
    wizsc9_opt3.pack(fill = 'both', expand = True)

    wizsc9_pla = tk.Button(wizsc9, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc9_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc9_pau = tk.Button(wizsc9, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc9_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc9_heli = tk.Label(wizsc9, image = health_icn, bd = 0, bg = 'white')
    wizsc9_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    wizsc9_helt = tk.Label(wizsc9, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc9_helt.place(x = 1916, y = 690, anchor = 'ne')

    wizsc9_armi = tk.Label(wizsc9, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    wizsc9_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    wizsc9_armt = tk.Label(wizsc9, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc9_armt.place(x = 1916, y = 790, anchor = 'ne')

    wizsc9_inv = tk.Button(wizsc9, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    wizsc9_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc9_ext = tk.Button(wizsc9, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    wizsc9_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc9";')
    con.commit()

    wizsc9.mainloop()



def wizstr10():
    
    global wizsc10

    try:
        wizsc6.after(500, lambda: wizsc6.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc10 = tk.Toplevel()
    wizsc10.attributes('-fullscreen', True)
    wizsc10.configure(bd = 1)

    wizsc10_can = tk.Canvas(wizsc10, width = 1920, height = 1080, bg = 'black')
    wizsc10_can.pack(expand = True, fill = 'both')

    wizsc10_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    wbg1 = ImageTk.PhotoImage(Image.open('{}Wagon.jpg'.format(ppath)))
    wizsc10_pic1 = tk.Label(wizsc10, image = wbg1, bd=5)
    wizsc10_pic1.place(x = 0, y = 0, anchor = 'nw')

    wbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 5.jpg'.format(wpath)))
    wizsc10_pic2 = tk.Label(wizsc10, image = wbg2, bd=5)
    wizsc10_pic2.place(x = 1320, y = 0, anchor = 'nw')

    wizsc10_fr1 = tk.Frame(wizsc10, width = 555, height = 365, bg = 'red')
    wizsc10_fr1.place(x = 15, y = 700, anchor = 'nw')
    wizsc10_fr1.propagate(0)

    wizsc10_opt1 = tk.Button(wizsc10_fr1, text = 'Attempt to\n Distract the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr12)
    wizsc10_opt1.pack(fill = 'both', expand = True)

    wizsc10_fr2 = tk.Frame(wizsc10, width = 555, height = 365, bg = 'blue')
    wizsc10_fr2.place(x = 575, y = 700, anchor = 'nw')
    wizsc10_fr2.propagate(0)

    wizsc10_opt2 = tk.Button(wizsc10_fr2, text = 'Attempt to\n Fight the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr11)
    wizsc10_opt2.pack(fill = 'both', expand = True)

    wizsc10_fr3 = tk.Frame(wizsc10, width = 550, height = 363, bg = 'green')
    wizsc10_fr3.place(x = 1135, y = 700, anchor = 'nw')
    wizsc10_fr3.propagate(0)

    wizsc10_opt3 = tk.Button(wizsc10_fr3, text = 'Hide and Hope\n that the Ogre\n Goes Away',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr13)
    wizsc10_opt3.pack(fill = 'both', expand = True)

    wizsc10_pla = tk.Button(wizsc10, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc10_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc10_pau = tk.Button(wizsc10, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc10_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc10_heli = tk.Label(wizsc10, image = health_icn, bd = 0, bg = 'white')
    wizsc10_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    wizsc10_helt = tk.Label(wizsc10, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc10_helt.place(x = 1916, y = 690, anchor = 'ne')

    wizsc10_armi = tk.Label(wizsc10, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    wizsc10_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    wizsc10_armt = tk.Label(wizsc10, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc10_armt.place(x = 1916, y = 790, anchor = 'ne')

    wizsc10_inv = tk.Button(wizsc10, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    wizsc10_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc10_ext = tk.Button(wizsc10, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    wizsc10_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc10";')
    con.commit()

    wizsc10.mainloop()



def wizstr11():
    
    global wizsc11

    try:
        wizsc6.after(500, lambda: wizsc6.destroy())
    except NameError:
        pass

    try:
        wizsc7.after(500, lambda: wizsc7.destroy())
    except NameError:
        pass

    try:
        wizsc9.after(500, lambda: wizsc9.destroy())
    except NameError:
        pass

    try:
        wizsc10.after(500, lambda: wizsc10.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc11 = tk.Toplevel()
    wizsc11.attributes('-fullscreen', True)
    wizsc11.configure(bd = 1)

    wizsc11_can = tk.Canvas(wizsc11, width = 1920, height = 1080, bg = 'black')
    wizsc11_can.pack(expand = True, fill = 'both')

    wizsc11_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    wbg1 = ImageTk.PhotoImage(Image.open('{}Ogre Fight.jpg'.format(ppath)))
    wizsc11_pic1 = tk.Label(wizsc11, image = wbg1, bd=5)
    wizsc11_pic1.place(x = 0, y = 0, anchor = 'nw')

    wbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 6.jpg'.format(wpath)))
    wizsc11_pic2 = tk.Label(wizsc11, image = wbg2, bd=5)
    wizsc11_pic2.place(x = 1320, y = 0, anchor = 'nw')

    wizsc11_fr1 = tk.Frame(wizsc11, width = 555, height = 365, bg = 'red')
    wizsc11_fr1.place(x = 15, y = 700, anchor = 'nw')
    wizsc11_fr1.propagate(0)

    wizsc11_opt1 = tk.Button(wizsc11_fr1, text = 'Poison\nthe Ogre',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = wizstr14)
    wizsc11_opt1.pack(fill = 'both', expand = True)

    wizsc11_fr2 = tk.Frame(wizsc11, width = 555, height = 365, bg = 'blue')
    wizsc11_fr2.place(x = 575, y = 700, anchor = 'nw')
    wizsc11_fr2.propagate(0)

    wizsc11_opt2 = tk.Button(wizsc11_fr2, text = 'Paralyze\nthe Ogre',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = wizstr15)
    wizsc11_opt2.pack(fill = 'both', expand = True)

    wizsc11_fr3 = tk.Frame(wizsc11, width = 550, height = 363, bg = 'green')
    wizsc11_fr3.place(x = 1135, y = 700, anchor = 'nw')
    wizsc11_fr3.propagate(0)

    wizsc11_opt3 = tk.Button(wizsc11_fr3, text = 'Use Your Knife\n to Attack',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr8)
    wizsc11_opt3.pack(fill = 'both', expand = True)

    wizsc11_pla = tk.Button(wizsc11, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc11_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc11_pau = tk.Button(wizsc11, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc11_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc11_heli = tk.Label(wizsc11, image = health_icn, bd = 0, bg = 'white')
    wizsc11_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    wizsc11_helt = tk.Label(wizsc11, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc11_helt.place(x = 1916, y = 690, anchor = 'ne')

    wizsc11_armi = tk.Label(wizsc11, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    wizsc11_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    wizsc11_armt = tk.Label(wizsc11, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc11_armt.place(x = 1916, y = 790, anchor = 'ne')

    wizsc11_inv = tk.Button(wizsc11, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    wizsc11_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc11_ext = tk.Button(wizsc11, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    wizsc11_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc11";')
    con.commit()

    wizsc11.mainloop()



def wizstr12():
    
    global wizsc12

    try:
        wizsc7.after(500, lambda: wizsc7.destroy())
    except NameError:
        pass

    try:
        wizsc9.after(500, lambda: wizsc9.destroy())
    except NameError:
        pass

    try:
        wizsc10.after(500, lambda: wizsc10.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc12 = tk.Toplevel()
    wizsc12.attributes('-fullscreen', True)
    wizsc12.configure(bd = 1)

    wizsc12_can = tk.Canvas(wizsc12, width = 1920, height = 1080, bg = 'black')
    wizsc12_can.pack(expand = True, fill = 'both')

    wizsc12_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    wbg1 = ImageTk.PhotoImage(Image.open('{}Wizard Story.jpg'.format(ppath)))
    wizsc12_pic1 = tk.Label(wizsc12, image = wbg1, bd=5)
    wizsc12_pic1.place(x = 0, y = 0, anchor = 'nw')

    wbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 7.jpg'.format(wpath)))
    wizsc12_pic2 = tk.Label(wizsc12, image = wbg2, bd=5)
    wizsc12_pic2.place(x = 1320, y = 0, anchor = 'nw')

    wizsc12_fr1 = tk.Frame(wizsc12, width = 555, height = 365, bg = 'red')
    wizsc12_fr1.place(x = 15, y = 700, anchor = 'nw')
    wizsc12_fr1.propagate(0)

    wizsc12_opt1 = tk.Button(wizsc12_fr1, font = ('Enchanted Land', 55),
                             text = 'Make a Clone of Yourself\nand Have it Distract\n the Ogre by Running\n Away from You',
                             bg = '#090D3A', fg = 'white', command = wizstr16)
    wizsc12_opt1.pack(fill = 'both', expand = True)

    wizsc12_fr2 = tk.Frame(wizsc12, width = 555, height = 365, bg = 'blue')
    wizsc12_fr2.place(x = 575, y = 700, anchor = 'nw')
    wizsc12_fr2.propagate(0)

    wizsc12_opt2 = tk.Button(wizsc12_fr2, text = 'Cast a Spell to Cover\nthe Surroundings\n in Smoke',
                            font = ('Enchanted Land', 70),
                            bg = '#090D3A', fg = 'white', command = wizstr17)
    wizsc12_opt2.pack(fill = 'both', expand = True)

    wizsc12_fr3 = tk.Frame(wizsc12, width = 550, height = 363, bg = 'green')
    wizsc12_fr3.place(x = 1135, y = 700, anchor = 'nw')
    wizsc12_fr3.propagate(0)

    wizsc12_opt3 = tk.Button(wizsc12_fr3, text = 'Throw a Big Rock\n in the Lake Nearby',
                            font = ('Enchanted Land', 75),
                            bg = '#090D3A', fg = 'white', command = wizstr8)
    wizsc12_opt3.pack(fill = 'both', expand = True)

    wizsc12_pla = tk.Button(wizsc12, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc12_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc12_pau = tk.Button(wizsc12, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc12_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc12_heli = tk.Label(wizsc12, image = health_icn, bd = 0, bg = 'white')
    wizsc12_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    wizsc12_helt = tk.Label(wizsc12, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc12_helt.place(x = 1916, y = 690, anchor = 'ne')

    wizsc12_armi = tk.Label(wizsc12, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    wizsc12_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    wizsc12_armt = tk.Label(wizsc12, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc12_armt.place(x = 1916, y = 790, anchor = 'ne')

    wizsc12_inv = tk.Button(wizsc12, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    wizsc12_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc12_ext = tk.Button(wizsc12, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    wizsc12_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc12";')
    con.commit()

    wizsc12.mainloop()




def wizstr13():
    
    global wizsc13

    try:
        wizsc7.after(500, lambda: wizsc7.destroy())
    except NameError:
        pass

    try:
        wizsc9.after(500, lambda: wizsc9.destroy())
    except NameError:
        pass

    try:
        wizsc10.after(500, lambda: wizsc10.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc13 = tk.Toplevel()
    wizsc13.attributes('-fullscreen', True)
    wizsc13.configure(bd = 1)

    wizsc13_can = tk.Canvas(wizsc13, width = 1920, height = 1080, bg = 'black')
    wizsc13_can.pack(expand = True, fill = 'both')

    wizsc13_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    wbg1 = ImageTk.PhotoImage(Image.open('{}Ogre Fight.jpg'.format(ppath)))
    wizsc13_pic1 = tk.Label(wizsc13, image = wbg1, bd=5)
    wizsc13_pic1.place(x = 0, y = 0, anchor = 'nw')

    wbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 8.jpg'.format(wpath)))
    wizsc13_pic2 = tk.Label(wizsc13, image = wbg2, bd=5)
    wizsc13_pic2.place(x = 1320, y = 0, anchor = 'nw')

    wizsc13_fr1 = tk.Frame(wizsc13, width = 555, height = 365, bg = 'red')
    wizsc13_fr1.place(x = 15, y = 700, anchor = 'nw')
    wizsc13_fr1.propagate(0)

    wizsc13_opt1 = tk.Button(wizsc13_fr1, text = 'Poison\nthe Ogre',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = wizstr14)
    wizsc13_opt1.pack(fill = 'both', expand = True)

    wizsc13_fr2 = tk.Frame(wizsc13, width = 555, height = 365, bg = 'blue')
    wizsc13_fr2.place(x = 575, y = 700, anchor = 'nw')
    wizsc13_fr2.propagate(0)

    wizsc13_opt2 = tk.Button(wizsc13_fr2, text = 'Paralyze\nthe Ogre',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = wizstr15)
    wizsc13_opt2.pack(fill = 'both', expand = True)

    wizsc13_fr3 = tk.Frame(wizsc13, width = 550, height = 363, bg = 'green')
    wizsc13_fr3.place(x = 1135, y = 700, anchor = 'nw')
    wizsc13_fr3.propagate(0)

    wizsc13_opt3 = tk.Button(wizsc13_fr3, text = 'Try to Stab\n the Ogre with\n Your Knife',
                            font = ('Enchanted Land', 70),
                            bg = '#090D3A', fg = 'white', command = wizstr8)
    wizsc13_opt3.pack(fill = 'both', expand = True)

    wizsc13_pla = tk.Button(wizsc13, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc13_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc13_pau = tk.Button(wizsc13, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc13_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc13_heli = tk.Label(wizsc13, image = health_icn, bd = 0, bg = 'white')
    wizsc13_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    wizsc13_helt = tk.Label(wizsc13, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc13_helt.place(x = 1916, y = 690, anchor = 'ne')

    wizsc13_armi = tk.Label(wizsc13, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    wizsc13_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    wizsc13_armt = tk.Label(wizsc13, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc13_armt.place(x = 1916, y = 790, anchor = 'ne')

    wizsc13_inv = tk.Button(wizsc13, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    wizsc13_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc13_ext = tk.Button(wizsc13, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    wizsc13_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc13";')
    con.commit()

    wizsc13.mainloop()



def wizstr14():
    
    global wizsc14

    try:
        wizsc11.after(500, lambda: wizsc11.destroy())
    except NameError:
        pass

    try:
        wizsc13.after(500, lambda: wizsc13.destroy())
    except NameError:
        pass

    try:
        wizsc17.after(500, lambda: wizsc17.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc14 = tk.Toplevel()
    wizsc14.attributes('-fullscreen', True)
    wizsc14.configure(bd = 1)

    wizsc14_can = tk.Canvas(wizsc14, width = 1920, height = 1080, bg = 'black')
    wizsc14_can.pack(expand = True, fill = 'both')
    
    wizsc14_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    wbg1 = ImageTk.PhotoImage(Image.open('{}Poison.jpg'.format(ppath)))
    wizsc14_pic1 = tk.Label(wizsc14, image = wbg1, bd=5)
    wizsc14_pic1.place(x = 0, y = 0, anchor = 'nw')

    wbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 9.jpg'.format(wpath)))
    wizsc14_pic2 = tk.Label(wizsc14, image = wbg2, bd=5)
    wizsc14_pic2.place(x = 1320, y = 0, anchor = 'nw')

    wizsc14_fr1 = tk.Frame(wizsc14, width = 555, height = 365, bg = 'red')
    wizsc14_fr1.place(x = 15, y = 700, anchor = 'nw')
    wizsc14_fr1.propagate(0)

    wizsc14_opt1 = tk.Button(wizsc14_fr1, text = 'Knock it\nUnconcious\n with Your Staff',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr16)
    wizsc14_opt1.pack(fill = 'both', expand = True)

    wizsc14_fr2 = tk.Frame(wizsc14, width = 555, height = 365, bg = 'blue')
    wizsc14_fr2.place(x = 575, y = 700, anchor = 'nw')
    wizsc14_fr2.propagate(0)

    wizsc14_opt2 = tk.Button(wizsc14_fr2, text = 'Use Your Knife to\nPut an End to\n the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr16)
    wizsc14_opt2.pack(fill = 'both', expand = True)

    wizsc14_fr3 = tk.Frame(wizsc14, width = 550, height = 363, bg = 'green')
    wizsc14_fr3.place(x = 1135, y = 700, anchor = 'nw')
    wizsc14_fr3.propagate(0)

    wizsc14_opt3 = tk.Button(wizsc14_fr3, text = 'Leave the Ogre\n and Let Time Put\n an End to it',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr8)
    wizsc14_opt3.pack(fill = 'both', expand = True)

    wizsc14_pla = tk.Button(wizsc14, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc14_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc14_pau = tk.Button(wizsc14, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc14_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc14_heli = tk.Label(wizsc14, image = health_icn, bd = 0, bg = 'white')
    wizsc14_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    wizsc14_helt = tk.Label(wizsc14, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc14_helt.place(x = 1916, y = 690, anchor = 'ne')

    wizsc14_armi = tk.Label(wizsc14, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    wizsc14_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    wizsc14_armt = tk.Label(wizsc14, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc14_armt.place(x = 1916, y = 790, anchor = 'ne')

    wizsc14_inv = tk.Button(wizsc14, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    wizsc14_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc14_ext = tk.Button(wizsc14, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    wizsc14_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc14";')
    con.commit()

    wizsc14.mainloop()



def wizstr15():
    
    global wizsc15

    try:
        wizsc11.after(500, lambda: wizsc11.destroy())
    except NameError:
        pass

    try:
        wizsc13.after(500, lambda: wizsc13.destroy())
    except NameError:
        pass

    try:
        wizsc17.after(500, lambda: wizsc17.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc15 = tk.Toplevel()
    wizsc15.attributes('-fullscreen', True)
    wizsc15.configure(bd = 1)

    wizsc15_can = tk.Canvas(wizsc15, width = 1920, height = 1080, bg = 'black')
    wizsc15_can.pack(expand = True, fill = 'both')
    
    wizsc15_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    wbg1 = ImageTk.PhotoImage(Image.open('{}Chains.jpg'.format(ppath)))
    wizsc15_pic1 = tk.Label(wizsc15, image = wbg1, bd=5)
    wizsc15_pic1.place(x = 0, y = 0, anchor = 'nw')

    wbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 10.jpg'.format(wpath)))
    wizsc15_pic2 = tk.Label(wizsc15, image = wbg2, bd=5)
    wizsc15_pic2.place(x = 1320, y = 0, anchor = 'nw')

    wizsc15_fr1 = tk.Frame(wizsc15, width = 555, height = 365, bg = 'red')
    wizsc15_fr1.place(x = 15, y = 700, anchor = 'nw')
    wizsc15_fr1.propagate(0)

    wizsc15_opt1 = tk.Button(wizsc15_fr1, text = 'Knock it\nUnconcious\n with Your Staff',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr16)
    wizsc15_opt1.pack(fill = 'both', expand = True)

    wizsc15_fr2 = tk.Frame(wizsc15, width = 555, height = 365, bg = 'blue')
    wizsc15_fr2.place(x = 575, y = 700, anchor = 'nw')
    wizsc15_fr2.propagate(0)

    wizsc15_opt2 = tk.Button(wizsc15_fr2, text = 'Use Your Knife\nto Put an End\nto the Ogre',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr16)
    wizsc15_opt2.pack(fill = 'both', expand = True)

    wizsc15_fr3 = tk.Frame(wizsc15, width = 550, height = 363, bg = 'green')
    wizsc15_fr3.place(x = 1135, y = 700, anchor = 'nw')
    wizsc15_fr3.propagate(0)

    wizsc15_opt3 = tk.Button(wizsc15_fr3, text = 'Make a\nRun for it',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = wizstr8)
    wizsc15_opt3.pack(fill = 'both', expand = True)

    wizsc15_pla = tk.Button(wizsc15, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc15_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc15_pau = tk.Button(wizsc15, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc15_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc15_heli = tk.Label(wizsc15, image = health_icn, bd = 0, bg = 'white')
    wizsc15_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    wizsc15_helt = tk.Label(wizsc15, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc15_helt.place(x = 1916, y = 690, anchor = 'ne')

    wizsc15_armi = tk.Label(wizsc15, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    wizsc15_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    wizsc15_armt = tk.Label(wizsc15, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc15_armt.place(x = 1916, y = 790, anchor = 'ne')

    wizsc15_inv = tk.Button(wizsc15, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    wizsc15_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc15_ext = tk.Button(wizsc15, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    wizsc15_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc15";')
    con.commit()

    wizsc15.mainloop()



def wizstr16():

    global wizsc16

    try:
        wizsc12.after(500, lambda: wizsc12.destroy())
    except NameError:
        pass

    try:
        wizsc14.after(500, lambda: wizsc14.destroy())
    except NameError:
        pass

    try:
        wizsc15.after(500, lambda: wizsc15.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc16 = tk.Toplevel()
    wizsc16.attributes('-fullscreen', True)
    wizsc16.configure(bd = 0)

    wizsc16_can = tk.Canvas(wizsc16, width = 1920, height = 1080, bg = 'black')
    wizsc16_can.pack(expand = True, fill = 'both')
    
    wbg1 = ImageTk.PhotoImage(Image.open('{}Parchment 6.jpg'.format(wpath)))
    wizsc16_can.create_image(0, 0, image = wbg1, anchor = 'nw')

    wizsc16_pla = tk.Button(wizsc16, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc16_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc16_pau = tk.Button(wizsc16, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc16_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc16_inv = tk.Button(wizsc16, text = 'Proceed', font = ('Enchanted Land', 33),
                         pady = 4, fg = 'white', bg =  'black', padx = 7)
    wizsc16_inv.place(x = 1916, y = 890, anchor = 'ne')

    wizsc16_ext = tk.Button(wizsc16,text = 'Exit', padx = 19, width = 5,
                           font = ('Enchanted Land', 33),
                           bg = 'black', fg = 'white', command = end_game)
    wizsc16_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc16";')
    con.commit()

    wizsc16.mainloop()



def wizstr17():
    
    global wizsc17

    try:
        wizsc12.after(500, lambda: wizsc12.destroy())
    except NameError:
        pass

    try:
        lodsc.after(500, lambda: lodsc.destroy())
        playsc.after(500, lambda: playsc.destroy())
    except NameError:
        pass

    wizsc17 = tk.Toplevel()
    wizsc17.attributes('-fullscreen', True)
    wizsc17.configure(bd = 1)

    wizsc17_can = tk.Canvas(wizsc17, width = 1920, height = 1080, bg = 'black')
    wizsc17_can.pack(expand = True, fill = 'both')
    
    wizsc17_can.create_image(0, 0, image = main_bg, anchor = 'nw')

    wbg1 = ImageTk.PhotoImage(Image.open('{}Smoke.jpg'.format(ppath)))
    wizsc17_pic1 = tk.Label(wizsc17, image = wbg1, bd=5)
    wizsc17_pic1.place(x = 0, y = 0, anchor = 'nw')

    wbg2 = ImageTk.PhotoImage(Image.open('{}Parchment Window 11.jpg'.format(wpath)))
    wizsc17_pic2 = tk.Label(wizsc17, image = wbg2, bd=5)
    wizsc17_pic2.place(x = 1320, y = 0, anchor = 'nw')

    wizsc17_fr1 = tk.Frame(wizsc17, width = 555, height = 365, bg = 'red')
    wizsc17_fr1.place(x = 15, y = 700, anchor = 'nw')
    wizsc17_fr1.propagate(0)

    wizsc17_opt1 = tk.Button(wizsc17_fr1, text = 'Poison\nthe Ogre',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = wizstr14)
    wizsc17_opt1.pack(fill = 'both', expand = True)

    wizsc17_fr2 = tk.Frame(wizsc17, width = 555, height = 365, bg = 'blue')
    wizsc17_fr2.place(x = 575, y = 700, anchor = 'nw')
    wizsc17_fr2.propagate(0)

    wizsc17_opt2 = tk.Button(wizsc17_fr2, text = 'Paralyze\nthe Ogre',
                            font = ('Enchanted Land', 100),
                            bg = '#090D3A', fg = 'white', command = wizstr15)
    wizsc17_opt2.pack(fill = 'both', expand = True)

    wizsc17_fr3 = tk.Frame(wizsc17, width = 550, height = 363, bg = 'green')
    wizsc17_fr3.place(x = 1135, y = 700, anchor = 'nw')
    wizsc17_fr3.propagate(0)

    wizsc17_opt3 = tk.Button(wizsc17_fr3, text = 'Attack the Ogre\n with Your Knife',
                            font = ('Enchanted Land', 80),
                            bg = '#090D3A', fg = 'white', command = wizstr8)
    wizsc17_opt3.pack(fill = 'both', expand = True)

    wizsc17_pla = tk.Button(wizsc17, image = play_img, bg = 'black', bd = 0, command = play_bgm)
    wizsc17_pla.place(x = 1865, y = 5, anchor = 'ne')

    wizsc17_pau = tk.Button(wizsc17, image = pause_img, bg = 'black', bd = 0, command = pause_bgm)
    wizsc17_pau.place(x = 1915, y = 5, anchor = 'ne')

    wizsc17_heli = tk.Label(wizsc17, image = health_icn, bd = 0, bg = 'white')
    wizsc17_heli.place(x = 1790, y = 690, anchor = 'ne')
    
    wizsc17_helt = tk.Label(wizsc17, text = '100', font = ('Enchanted Land', 55),
                           bg = 'red', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc17_helt.place(x = 1916, y = 690, anchor = 'ne')

    wizsc17_armi = tk.Label(wizsc17, image = armour_icn, bd = 0, bg = 'white', padx = 5, pady = 5)
    wizsc17_armi.place(x = 1790, y = 790, anchor = 'ne')
    
    wizsc17_armt = tk.Label(wizsc17, text = '000', font = ('Enchanted Land', 55),
                           bg = 'blue', fg = 'white', bd = 0, padx = 30, pady = 9)
    wizsc17_armt.place(x = 1916, y = 790, anchor = 'ne')

    wizsc17_inv = tk.Button(wizsc17, text = 'Inventory', font = ('Enchanted Land', 33),
                           width = 12, pady = 4, fg = 'white', bg =  '#272625', command = inventory)
    wizsc17_inv.place(x = 1916, y = 890, anchor = 'ne')
    
    wizsc17_ext = tk.Button(wizsc17, text = 'Exit', padx = 19, width = 10,
                           font = ('Enchanted Land', 33),
                           bg = '#272625', fg = 'white', command = end_game)
    wizsc17_ext.place(x = 1916, y = 1076, anchor = 'se')

    cur.execute('update progress set story_progress = "wizsc17";')
    con.commit()

    wizsc17.mainloop()

sqlsc_win()
