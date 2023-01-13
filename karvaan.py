#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:48:28 2023

@author: sanatwalia
"""

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
        self.control_widget()

    def frames(self):
        self.track = tk.LabelFrame(self, text="𝔐𝔲𝔰𝔦𝔠", font=("Gothic", 20, "bold"),
                                   bg="brown", fg="black", bd=10, relief=tk.GROOVE)
        self.track.configure(width=720, height=500)
        self.track.grid(row=0, column=0, padx=10)

        self.tracklist = tk.LabelFrame(self, text=f'𝔓𝔩𝔞𝔶𝔩𝔦𝔰𝔱-{len(self.playlist)}',
                                       font=("Gothic", 20, "bold"), bg="black", fg="white",
                                       bd=10, relief=tk.GROOVE)
        self.tracklist.configure(width=220, height=620)
        self.tracklist.grid(row=0, column=1, rowspan=3)

        self.control = tk.LabelFrame(self, text="𝔠𝔬𝔫𝔱𝔯𝔬𝔩𝔰", font=("Gothic", 20, "bold"),
                                     bg="grey", fg="black", bd=10, relief=tk.GROOVE)
        self.control.configure(width=720, height=120)
        self.control.grid(row=2, column=0, pady=5, padx=10)

    def track_widget(self):

        self.canvas = tk.Label(self.track, image=img)
        self.canvas.configure(width=700, height=440)
        self.canvas.grid(row=0, column=0)
        self.canvas = tk.Label(self.track, font=(
            "gothic", 16), bg="black", fg="green")
        self.canvas['text'] = "𝔎𝔞𝔯𝔙𝔞𝔞𝔫 𝔐𝔲𝔰𝔦𝔠 𝔓𝔩𝔞𝔶𝔢𝔯"
        self.canvas.configure(width=60, height=2)
        self.canvas.grid(row=1, column=0)

    def control_widget(self):
        self.load_songs = tk.Button(
            self.control, bg="white", fg="black", font=10)
        self.load_songs['text'] = '𝔏𝔬𝔞𝔡 𝔰𝔬𝔫𝔤𝔰'
        self.load_songs['command']=self.retrieve_songs
        self.load_songs.grid(row=0, column=0, padx=10)

        self.prev = tk.Button(self.control, imag=prev)
        self.prev['command']=self.prev_song
        self.prev.grid(row=0, column=1)

        self.pause = tk.Button(self.control, image=play)
        self.pause['command']=self.pause_song
        self.pause.grid(row=0, column=2)

        self.next = tk.Button(self.control, image=next_)
        self.next['command']=self.next_song
        self.next.grid(row=0, column=3)

        self.volume = tk.DoubleVar()
        self.slider = tk.Scale(self.control, from_=0,
                               to=100, orient=tk.HORIZONTAL)
        self.slider['variable'] = self.volume
        self.slider.set(7)
        self.slider.grid(row=0,column=6,padx=5)
    def tracklist_widgets(self):
        self.scrollbar=tk.Scrollbar(self.tracklist,orient=tk.VERTICAL )
        self.scrollbar.grid(row=0,column=1,rowspan=9,sticky='ns')
        
    
    def retrieve_songs():
        pass
    
    def pause_song(self):
        pass
    
    def prev_song(self):
        pass
    def next_song(self):
        pass
    def change_volume(self,event=None):
        
        self.v=self.volume.get()
    


root = tk.Tk()
root.geometry("970x650")
root.wm_title("𝔎𝔞𝔯𝔙𝔞𝔞𝔫")
img = PhotoImage(file='/Users/sanatwalia/Desktop/karvaan/osdc_projrct_karvaan/pic4.gif')
prev = PhotoImage(file='/Users/sanatwalia/Desktop/karvaan/prev.gif')
play = PhotoImage(file='/Users/sanatwalia/Desktop/karvaan/play.gif')
next_ = PhotoImage(file='/Users/sanatwalia/Desktop/karvaan/next.gif')

player = karvaan(master=root)
player.mainloop()
