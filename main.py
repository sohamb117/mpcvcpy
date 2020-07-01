import curses
import os

## CONSTANTS ##
splitList = ['(',',','[',';','\n']
title = ""
artist = ""
album = ""
play = ""
rand = ""
sing = ""
rep = ""

## SONG INFO ##
def trimmer(name):
    for idx in splitList:
        if idx in name:
            name = name.split(idx)[0]
    return(name)

def fetchSong():
    global title, album, artist
    title = os.popen('mpc current -f %title%').read()
    artist = os.popen('mpc current -f %artist%').read()
    album = os.popen('mpc current -f %album%').read()
    title = trimmer(title)
    artist = trimmer(artist)
    album = trimmer(album)


## STATES ##
def fetchState():
    global play, rep, rand, sing
    state = os.popen('mpc').read()
    play = state.split('[')[1].split(']')[0]
    rep = state.split("repeat: ")[1].split(' ')[0]
    rand = state.split("random: ")[1].split(' ')[0]
    sing = state.split("single: ")[1].split(' ')[0]

## CURSES FUNCTIONS ##
def centerText(stdscr, text, y):
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2 + 1
    stdscr.addstr(y, x, text)

def highlight(position, text):
    print(position)

def draw(stdscr):
    centerText(stdscr, title, 5)
    centerText(stdscr, artist, 6)
    centerText(stdscr, album, 7)
    centerText(stdscr, play, 8)
    state = ("Repeat: " + rep + " | Random: " + rand + " | Single: " + sing)
    centerText(stdscr, state, 9)


def wrapper(stdscr):
    curses.curs_set(0)
    curses.use_default_colors()
    stdscr.clear()
    fetchSong()
    fetchState()
    draw(stdscr)
    stdscr.refresh()

while True:
    curses.wrapper(wrapper)
