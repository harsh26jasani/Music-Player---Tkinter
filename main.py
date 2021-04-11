from tkinter import *
import os
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer

root = Tk()

# creating menubar
menubar = Menu(root)
root.config(menu=menubar)


# open a new browsing window for selecting music of your choice
def browse_file():
    global filename
    filename = filedialog.askopenfile()


# creating sub-menu
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo("About Melody", "This is a music player built using Python Tkinter by Harsh Jasani")


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About us", command=about_us)

mixer.init()  # initializing the mixer

# root.geometry("300x300")  # size of window
root.title("Melody")  # title of window
root.iconbitmap(r"melody.ico")  # icon of window

text = Label(root, text="Let's get this party started...!!")  # text on window
text.pack(pady=10)  # makes text visible on window


def play_music():
    try:
        paused  # checks whether paused variable is initialized or not.
    except NameError:  # if not initialized then executes the code under except condition
        try:
            mixer.music.load(filename)  # replace party.mp3 with filename to browse music
            mixer.music.play()
            statusbar["text"] = "Playing music" + " " + os.path.basename(filename.name)
        except:
            tkinter.messagebox.showerror("File not found.", "Melody couldn't find a file. Please check again..!!")
    else:  # if initialized then it goes to the else condition
        mixer.music.unpause()
        statusbar["text"] = "Music resumed.."


def stop_music():
    mixer.music.stop()
    statusbar["text"] = "Music stopped."


def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar["text"] = "Music paused.."


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)
    # set_volume takes value from 0 to 1. So we divide by 100.


# used for arranging buttons horizontally, pad is used for arranging properly
middleframe = Frame(root)
middleframe.pack(padx=10, pady=10)

playPhoto = PhotoImage(file="play.png")  # path of image using inbuilt function
playBtn = Button(middleframe, image=playPhoto, command=play_music)  # adding button using above image
playBtn.pack(side=LEFT, padx=10)

stopPhoto = PhotoImage(file="stop.png")
stopBtn = Button(middleframe, image=stopPhoto, command=stop_music)
stopBtn.pack(side=LEFT, padx=10)

pausePhoto = PhotoImage(file="pause.png")
pauseBtn = Button(middleframe, image=pausePhoto, command=pause_music)
pauseBtn.pack(side=LEFT, padx=10)

# scale is a volume widget
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(75)
mixer.music.set_volume(0.75)
scale.pack(pady=15)

# creating statusbar
statusbar = Label(root, text="Welcome to Melody", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
