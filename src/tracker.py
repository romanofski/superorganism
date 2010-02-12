#!/usr/bin/env python
# Copyright 2010 Roman Joost <roman@bromeco.de>
# Tracker a prototype of a meta-tracker implementation
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
import sys
import getopt
import metatracker


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hl", ["help", "list"])
    except getopt.GetoptError, err:
        print "Option not recognized."
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-l', '--list')
            tracker = metatracker.Tracker()
            tracker.list()
        else:
            usage()
            sys.exit(2)


def usage():
    print """tracker.py - Copyright 2010 Roman Joost
The metatracker program lets you edit, list and manager your bugs
including synchronizing to other trackers.

usage: tracker option

    options:    value:
        list    lists all bugs"""

    

if __name__ == "__main__":
    main()
