import time
import os
import pickle
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer


class karvaan(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.playlist = []

        self.frames()
        self.track_widget()

    def frames(self):
        self.track = tk.LabelFrame(self, text="Music", font=("Gothic", 20, "bold"),
                                   bg="brown", fg="black", bd=10, relief=tk.GROOVE)
        self.track.configure(width=720, height=500)
        self.track.grid(row=0, column=0, padx=10)

        self.tracklist = tk.LabelFrame(self, text=f'Playlist-{len(self.playlist)}',
                                       font=("Gothic", 20, "bold"), bg="black", fg="white",
                                       bd=10, relief=tk.GROOVE)
        self.tracklist.configure(width=220, height=620)
        self.tracklist.grid(row=0, column=1, rowspan=3)

        self.control = tk.LabelFrame(self, text="CONTROLS", font=("Gothic", 20, "bold"),
                                     bg="grey", fg="black", bd=10, relief=tk.GROOVE)
        self.control.configure(width=720, height=120)
        self.control.grid(row=2, column=0, pady=5, padx=10)

    def track_widget(self):
        self.canvas = tk.Label(self.track, image=img7)
        self.canvas.configure(width=700, height=440)
        self.canvas.grid(row=0, column=0)


root = tk.Tk()
root.geometry("970x650")
root.wm_title("KarVaan")

img1 = PhotoImage(file='/Users/sanatwalia/Desktop/python /karvaan/pic1.gif')
img2 = PhotoImage(file='/Users/sanatwalia/Desktop/python /karvaan/pic2.gif')
img3 = PhotoImage(file='/Users/sanatwalia/Desktop/python /karvaan/pic3.gif')
img4 = PhotoImage(file='/Users/sanatwalia/Desktop/python /karvaan/pic4.gif')
img5 = PhotoImage(file='/Users/sanatwalia/Desktop/python /karvaan/pic5.gif')
img6 = PhotoImage(file='/Users/sanatwalia/Desktop/python /karvaan/pic6.gif')
img7 = PhotoImage(file='/Users/sanatwalia/Desktop/python /karvaan/pic7.gif')
img8 = PhotoImage(file='/Users/sanatwalia/Desktop/python /karvaan/pic8.gif')
img9 = PhotoImage(file='/Users/sanatwalia/Desktop/python /karvaan/pic9.gif')
img10 = PhotoImage(file='/Users/sanatwalia/Desktop/python /karvaan/pic10.gif')
img11 = PhotoImage(file='/Users/sanatwalia/Desktop/python /karvaan/pic11.gif')
img12 = PhotoImage(file='/Users/sanatwalia/Desktop/python /karvaan/pic12.gif')
images = [img1, img2, img3, img4, img5, img6,
          img7, img8, img9, img10, img11, img12]

player = karvaan(master=root)
player.mainloop()
