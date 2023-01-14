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
    def _init_(self, master=None):
        super()._init_(master)
        self.master = master
        self.pack()
        mixer.init()

        if os.path.exists('songs.pickle'):
            with open('songs.pickle', 'rb') as f:
                self.playlist = pickle.load(f)
        else:
            self.playlist = []

        self.current = 0
        self.paused = True
        self.played = False

        self.frames()
        self.track_widgets()
        self.control_widgets()
        self.tracklist_widgets()

    def frames(self):
        self.track = tk.LabelFrame(self, text='𝔐𝔲𝔰𝔦𝔠',
                                   font=("Gothic", 20, "bold"),
                                   bg="brown", fg="black", bd=10, relief=tk.GROOVE)

        self.track.configure(width=720, height=500)
        self.track.grid(row=0, column=0, padx=10)

        self.tracklist = tk.LabelFrame(self, text=f'𝔓𝔩𝔞𝔶𝔩𝔦𝔰𝔱 - {str(len(self.playlist))}',
                                       font=("Gothic", 20, "bold"),
                                       bg="black", fg="white", bd=10, relief=tk.GROOVE)
        self.tracklist.configure(width=220, height=620)
        self.tracklist.grid(row=0, column=1, rowspan=3)

        self.controls = tk.LabelFrame(self, text="𝔠𝔬𝔫𝔱𝔯𝔬𝔩𝔰",
                                      font=("times new roman", 20, "bold"),
                                      bg="grey", fg="black", bd=10, relief=tk.GROOVE)
        self.controls.configure(width=720, height=120)
        self.controls.grid(row=2, column=0, pady=5, padx=10)

    def track_widgets(self):
        self.canvas = tk.Label(self.track, image=img)
        self.canvas.configure(width=700, height=440)
        self.canvas.grid(row=0, column=0)

        self.songtrack = tk.Label(self.track, font=("gothic", 16, "bold"),
                                  bg="black", fg="green")
        self.songtrack['text'] = '𝔎𝔞𝔯𝔙𝔞𝔞𝔫 𝔐𝔲𝔰𝔦𝔠 𝔓𝔩𝔞𝔶𝔢𝔯'
        self.songtrack.config(width=60, height=2)
        self.songtrack.grid(row=1, column=0, padx=10)

    def control_widgets(self):
        self.loadSongs = tk.Button(
            self.controls, bg='white', fg='black', font=10)
        self.loadSongs['text'] = '𝔏𝔬𝔞𝔡 𝔰𝔬𝔫𝔤𝔰'
        self.loadSongs['command'] = self.retrieve_songs
        self.loadSongs.grid(row=0, column=0, padx=10)

        self.prev = tk.Button(self.controls, image=prev)
        self.prev['command'] = self.prev_song
        self.prev.grid(row=0, column=1)

        self.pause = tk.Button(self.controls, image=pause)
        self.pause['command'] = self.pause_song
        self.pause.grid(row=0, column=4)

        self.next = tk.Button(self.controls, image=next_)
        self.next['command'] = self.next_song
        self.next.grid(row=0, column=7)

        self.volume = tk.DoubleVar(self)
        self.slider = tk.Scale(self.controls, from_=0,
                               to=100, orient=tk.HORIZONTAL)
        self.slider['variable'] = self.volume
        self.slider.set(47)
        mixer.music.set_volume(0.8)
        self.slider['command'] = self.change_volume
        self.slider.grid(row=0, column=10, padx=5)

    def tracklist_widgets(self):
        self.scrollbar = tk.Scrollbar(self.tracklist, orient=tk.VERTICAL)
        self.scrollbar.grid(row=0, column=1, rowspan=9, sticky='ns')

        self.list = tk.Listbox(self.tracklist, selectmode=tk.SINGLE,
                               yscrollcommand=self.scrollbar.set, selectbackground='red')
        self.enumerate_songs()
        self.list.config(height=32)
        self.list.bind('<Double-1>', self.play_song)

        self.scrollbar.config(command=self.list.yview)
        self.list.grid(row=0, column=0, rowspan=12)

    def retrieve_songs(self):
        self.songlist = []
        directory = filedialog.askdirectory()
        for root_, dirs, files in os.walk(directory):
            for file in files:
                if os.path.splitext(file)[1] == '.mp3':
                    path = (root_ + '/' + file).replace('\\', '/')
                    self.songlist.append(path)

        with open('songs.pickle', 'wb') as f:
            pickle.dump(self.songlist, f)
        self.playlist = self.songlist
        self.tracklist['text'] = f'PlayList - {str(len(self.playlist))}'
        self.list.delete(0, tk.END)
        self.enumerate_songs()

    def enumerate_songs(self):
        for index, song in enumerate(self.playlist):
            self.list.insert(index, os.path.basename(song))

    def play_song(self, event=None):
        if event is not None:
            self.current = self.list.curselection()[0]
            for i in range(len(self.playlist)):
                self.list.itemconfigure(i, bg="white")

        print(self.playlist[self.current])
        mixer.music.load(self.playlist[self.current])
        self.songtrack['anchor'] = 'w'
        self.songtrack['text'] = os.path.basename(self.playlist[self.current])

        self.pause['image'] = play
        self.paused = False
        self.played = True
        self.list.activate(self.current)
        self.list.itemconfigure(self.current, bg='sky blue')

        mixer.music.play()

    def pause_song(self):
        if not self.paused:
            self.paused = True
            mixer.music.pause()
            self.pause['image'] = pause
        else:
            if self.played == False:
                self.play_song()
            self.paused = False
            mixer.music.unpause()
            self.pause['image'] = play

    def prev_song(self):
        if self.current > 0:
            self.current -= 1
        else:
            self.current = 0
        self.list.itemconfigure(self.current + 1, bg='white')
        self.play_song()

    def next_song(self):
        if self.current < len(self.playlist) - 1:
            self.current += 1
        else:
            self.current = 0
        self.list.itemconfigure(self.current - 1, bg='white')
        self.play_song()

    def change_volume(self, event=None):
        self.v = self.volume.get()
        mixer.music.set_volume(self.v / 10)


root = tk.Tk()
root.geometry('970x650')
root.wm_title('𝔎𝔞𝔯𝔙𝔞𝔞𝔫')

img = PhotoImage(file='images/music.png')
next_ = PhotoImage(file='images/next.gif')
prev = PhotoImage(file='images/previous.gif')
play = PhotoImage(file='images/play.gif')
pause = PhotoImage(file='images/pause.gif')

player = karvaan(master=root)
player.mainloop()

