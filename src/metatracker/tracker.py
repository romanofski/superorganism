#!/usr/bin/env python
import test
import sys
import traceback
import curses
import string

sys.path[0:0] = [
  '/home/roman/works/projects/metatracker/src',
  '/home/roman/buildout-eggs/nose-0.11.1-py2.4.egg',
  '/home/roman/buildout-eggs/setuptools-0.6c9-py2.4.egg',
  '/home/roman/buildout-eggs/ZODB3-3.9.0b1-py2.4-linux-i686.egg',
  '/home/roman/buildout-eggs/zope.testing-3.7.6-py2.4.egg',
  '/home/roman/buildout-eggs/zope.proxy-3.5.0-py2.4-linux-i686.egg',
  '/home/roman/buildout-eggs/zope.interface-3.5.1-py2.4-linux-i686.egg',
  '/home/roman/buildout-eggs/zope.event-3.4.1-py2.4.egg',
  '/home/roman/buildout-eggs/zdaemon-2.0.4-py2.4.egg',
  '/home/roman/buildout-eggs/ZConfig-2.6.1-py2.4.egg',
  '/home/roman/buildout-eggs/zc.lockfile-1.0.0-py2.4.egg',
  '/home/roman/buildout-eggs/transaction-1.0a1-py2.4.egg',
  ]
hotkey_attr = curses.A_BOLD | curses.A_UNDERLINE
menu_attr = curses.A_NORMAL
EXIT = 0
CONTINUE = 1
counter = 0
cfg_dict = {'target': 'DEFAULT.HTML',
            'source': 'txt2html.txt',
            'type':   'INFER',
            'proxy':  'NONE' }

def main(stdscr):
    global screen
    screen = stdscr.subwin(23, 79, 0, 0)
    screen.box()
    screen.hline(2, 1, curses.ACS_HLINE, 77)
    screen.refresh()

    # Define the topbar menus
    file_menu = ("File","file_func()")
    exit_menu = ("Exit", "EXIT")
    # Add the topbar menus to screen object
    topbar_menu((file_menu, exit_menu))

    # Enter the topbar menu loop
    while topbar_key_handler():
        draw_dict()

def topbar_menu(menus):
    left = 2
    for menu in menus:
        menu_name = menu[0]
        menu_hotkey = menu_name[0]
        menu_no_hot = menu_name[1:]
        screen.addstr(1, left, menu_hotkey, hotkey_attr)
        screen.addstr(1, left+1, menu_no_hot, menu_attr)
        left = left + len(menu_name) + 3
        # Add key handlers for this hotkey
        topbar_key_handler((string.upper(menu_hotkey), menu[1]))
        topbar_key_handler((string.lower(menu_hotkey), menu[1]))
    # Little aesthetic thing to display application title
    screen.addstr(1, left-1,
                  ">"*(52-left)+ " Txt2Html Curses Interface",
                  curses.A_STANDOUT)
    screen.refresh()

#-- Display the currently selected options
def draw_dict():
    screen.addstr(5,33, " "*43, curses.A_NORMAL)
    screen.addstr(8,33, " "*43, curses.A_NORMAL)
    screen.addstr(11,33, " "*43, curses.A_NORMAL)
    screen.addstr(14,33, " "*43, curses.A_NORMAL)
    screen.addstr(5, 33, cfg_dict['source'], curses.A_STANDOUT)
    screen.addstr(8, 33, cfg_dict['target'], curses.A_STANDOUT)
    screen.addstr(11,33, cfg_dict['type'], curses.A_STANDOUT)
    screen.addstr(14,33, cfg_dict['proxy'], curses.A_STANDOUT)
    screen.addstr(17,33, str(counter), curses.A_STANDOUT)
    screen.refresh()

def file_func():
    s = curses.newwin(5,10,2,1)
    s.box()
    s.addstr(1,2, "I", hotkey_attr)
    s.addstr(1,3, "nput", menu_attr)
    s.addstr(2,2, "O", hotkey_attr)
    s.addstr(2,3, "utput", menu_attr)
    s.addstr(3,2, "T", hotkey_attr)
    s.addstr(3,3, "ype", menu_attr)
    s.addstr(1,2, "", hotkey_attr)
    s.refresh()
    c = s.getch()
    if c in (ord('I'), ord('i'), curses.KEY_ENTER, 10):
        curses.echo()
        s.erase()
        screen.addstr(5,33, " "*43, curses.A_UNDERLINE)
        cfg_dict['source'] = screen.getstr(5,33)
        curses.noecho()
    else:
        curses.beep()
        s.erase()
        return CONTINUE

def topbar_key_handler(key_assign=None, key_dict={}):
    if key_assign:
        key_dict[ord(key_assign[0])] = key_assign[1]
    else:
        c = screen.getch()
        if c in (curses.KEY_END, ord('!')):
            return 0
        elif c not in key_dict.keys():
            curses.beep()
            return 1
        else:
            return eval(key_dict[c])

if __name__ == '__main__':
    try:
        # Initialize curses
        stdscr=curses.initscr()
        #curses.start_color()
        # Turn off echoing of keys, and enter cbreak mode,
        # where no buffering is performed on keyboard input
        curses.noecho() ; curses.cbreak()

        # In keypad mode, escape sequences for special keys
        # (like the cursor keys) will be interpreted and
        # a special value like curses.KEY_LEFT will be returned
        stdscr.keypad(1)
        main(stdscr)                    # Enter the main loop
        # Set everything back to normal
        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()                 # Terminate curses
    except:
        # In the event of an error, restore the terminal
        # to a sane state.
        stdscr.keypad(0)
        curses.echo() ; curses.nocbreak()
        curses.endwin()
        traceback.print_exc()           # Print the exception
