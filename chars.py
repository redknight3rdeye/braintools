# I use this script with Konsole and the Symbola font, it's very
# pleasing to look at (but does not print the shell very usably,
# so you may have to limp into the directory to run it)
#
# Also you have to use Symbola or all of the weird unicode stuff
# will just be unreadable blocks of nothing

import random
import curses
import time    # unused


chars = []
for r in [
        ## Configuration file   ##
        range(0x00000, 0x0024F), # latin
        range(0x00250, 0x002AF), # IPA
        range(0x00400, 0x00527), # cyrillic
        range(0x00591, 0x005F4), # hebrew
        range(0x00600, 0x006FF), # arabic
        range(0x016A0, 0x016F0), # runic
        range(0x02200, 0x022FF), # math
        range(0x02300, 0x026FF), # misc technical and stuff
        range(0x02701, 0x027BF), # dingbats
        range(0x101D0, 0x101FD), # phaistos disc
        range(0x1F700, 0x1F773), # alchemical
]:
    chars += [chr(i) for i in r if chr(i).isprintable()]

def main(stdscr):
    curses.curs_set(False)
    stdscr.clear()
    curses.halfdelay(47) # <- beautiful

    paused = False
    while True:
        for l in range(curses.LINES-1):
            if paused: continue
            stdscr.addstr(l, 0, "".join(
                [chars[random.randint(0, len(chars)-1)]
                 for i in range(curses.COLS - 7)])
            )
        if stdscr.getch() != -1: paused = not paused


curses.wrapper(main)
curses.curs_set(True)
