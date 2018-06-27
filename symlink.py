#! /usr/bin/python

__title__ = "SYMLINK"
__description__ = "Symlink script for python2x: Create and remove symlink quickly in the current directory."
__copyrigth__ = "Copyright (c) 2017 Massimiliano Ranauro (huckbit@gmail.com)"
__author__ = "Massimiliano RANAURO"
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Massimiliano RANAURO"
__email__ = "huckbit@huckbit.com"
__status__ = "Production"

import os
import json

with open(os.getcwd() + '/settings.json') as json_data_file:
    settings = json.load(json_data_file)

# global variables
currentPath = os.getcwd()
dest = currentPath + "/" + settings["dir_name"]


# Print header and current status
def header():
    print """
====================================
LINK/UNLINK DOCROOT for Python 2.x
====================================
[1] - create link for a folder
[2] - unlink folder
[l] - list current folders
[q] - quit
"""
    if os.path.exists(dest):
        print "Currents Status: >>> LINK EXISTS \n"
    else:
        print "Current Status: >>> LINK DOESN'T EXISTS \n"


# function for removing the link to public_html
def removeLink(dest):
    os.system("clear")
    if os.path.exists(dest):

        # unlink public_html
        os.unlink(dest)

        if not os.path.exists(dest):
            os.system("clear")
            print ">>> Link removed"
            print ""
            raw_input("Press Enter to continue...")

    else:
        print("Error: I can't unlink! Link doesn't exists \n")
        raw_input("Press Enter to continue...")


# function for creating the link to public_html from the source path
def createLink(path, dest):
    os.system("clear")

    # get only the dir inside the path
    directories = [d for d in os.listdir('.') if os.path.isdir(d)]

    # list with option and value for the directories
    for i, directory in enumerate(directories):
        print(i, directory)

    if directories:
        option = int(input("insert the number of the folder you want to link: "))

        # create the source path with the folder name
        src = currentPath + "/" + (directories[option])

        # create the symlink
        os.symlink(src, dest)

        # if the symlink is created
        if os.path.islink(dest):
            print ">>> Link created \n"
            raw_input("Press Enter to continue...")
        else:
            print ">>> Error creating link \n"
            raw_input("Press Enter to continue...")

    else:
        print("Error: Import your project folder before to create a link to it. \n")
        raw_input("Press Enter to continue...")


def menu():
    exit = True
    while exit:
        os.system("clear")
        header()
        option = raw_input("what would you like to do? ")

        # create the link
        if option == '1':
            createLink(currentPath, dest)

        # remove the link
        elif option == '2':
            removeLink(dest)

        # list current directory
        elif option == 'l':
            os.system("clear")
            os.system("ls -altr")
            raw_input("Press Enter to continue...")

        # quit
        elif option == 'q':
            os.system("clear")
            print "Thanks for using link/unlik. Bye!"
            exit = False

        # exceptions
        else:
            os.system("clear")
            print "ERROR: This option is not available! \n"
            raw_input("Press Enter to continue...")


# start the script
menu()
