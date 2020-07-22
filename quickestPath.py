## -*- coding: utf-8 -*-

from tkinter import *
from node import Node
from gui import GUI

def main():
    gui = GUI(25, 10, 700)

    gui.init_checkBox()
    gui.init_button()
    gui.create_grid()
    gui.run()

if __name__ == "__main__":
    main()
