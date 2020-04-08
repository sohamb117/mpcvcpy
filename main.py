import curses
import os

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
plArtist = os.popen('mpc playlist -f %title%').read()
plArtistList = []

def playlistTrim(playlist):
    playlistList = playlist.split('\n')
    for x in range(0, len(playlistList)):
        playlistList[x] = trimmer(playlistList[x])
    return (playlistList)

plTitleList = playlistTrim(plTitle)
plArtistList = playlistTrim(plArtist)
