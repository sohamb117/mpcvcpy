import curses
import os
import time

## CONSTANTS ##
splitList = [':','(',',','[',';','\n']
title = ""
artist = ""
album = ""
plTitle = ""
plArtist = ""
state = ""
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
    title = os.popen('mpc current -f %title%').read()
    artist = os.popen('mpc current -f %artist%').read()
    album = os.popen('mpc current -f %album%').read()
    title = trimmer(title)
    artist = trimmer(artist)
    album = trimmer(album)


## PLAYLIST ##

def playlistTrim(playlist):
    playlistList = playlist.split('\n')
    for x in range(0, len(playlistList)):
        playlistList[x] = trimmer(playlistList[x])
    return (playlistList)

def fetchPlaylist():
    plTitle = os.popen('mpc playlist -f %title%').read()
    plTitleList = []
    plArtist = os.popen('mpc playlist -f %artist%').read()
    plArtistList = []
    plTitleList = playlistTrim(plTitle)
    plArtistList = playlistTrim(plArtist)


## STATES ##
def fetchState():
    state = os.popen('mpc').read()
    play = state.split('[')[1].split(']')[0] 
    rep = state.split("repeat: ")[1].split(' ')[0] 
    rand = state.split("random: ")[1].split(' ')[0]
    sing = state.split("single: ")[1].split(' ')[0]


## CURSES FUNCTIONS ##

def wrapper(stdscr):
    curses.curs_set(0)
    curses.use_default_colors()
    stdscr.clear()
    stdscr.addstr(0, 0, title)
    stdscr.refresh()
    time.sleep(5)
curses.wrapper(wrapper)
