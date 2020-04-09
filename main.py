import curses
import os

state = os.popen('mpc').read()
title = os.popen('mpc current -f %title%').read()
artist = os.popen('mpc current -f %artist%').read()
album = os.popen('mpc current -f %album%').read()
splitList = [':','(',',','[',';','\n']
def trimmer(name):
    for idx in splitList:
        if idx in name:
            name = name.split(idx)[0]
    return(name)
print(trimmer(title))
print(trimmer(artist))
print(trimmer(album))

## PLAYLIST ##
plTitle = os.popen('mpc playlist -f %title%').read()
plTitleList = []
plArtist = os.popen('mpc playlist -f %artist%').read()
plArtistList = []

def playlistTrim(playlist):
    playlistList = playlist.split('\n')
    for x in range(0, len(playlistList)):
        playlistList[x] = trimmer(playlistList[x])
    return (playlistList)

plTitleList = playlistTrim(plTitle)
plArtistList = playlistTrim(plArtist)

print(plTitleList)
print(plArtistList)
## STATES ##
play = state.split('[')[1].split(']')[0] 
rep = state.split("repeat: ")[1].split(' ')[0] 
rand = state.split("random: ")[1].split(' ')[0]
sing = state.split("single: ")[1].split(' ')[0]

print(play, rep, rand, sing)
