from tkinter import *

import core

class GUI:
    """
    py2048 GUI
    """
    windowtitle = "py2048"
    tilesize = 50
    tilepadding = 5
    topheight = 50
    bottomheight = 50

    def __init__(self, core):
        self.core = core

        self.window = Tk()
        self.window.title(GUI.windowtitle)

        self.windowwidth = self.core.board_width * GUI.tilesize + (self.core.board_width + 1) * GUI.tilepadding
        self.windowheight = self.core.board_height * GUI.tilesize + (self.core.board_height + 1) * GUI.tilepadding + GUI.topheight + GUI.bottomheight

        self.window.geometry(str(self.windowwidth) + "x" + str(self.windowheight) + "+100+100")
        self.window.resizable(True, True)

        self.topframe = Frame(self.window, height=GUI.topheight)
        self.topframe.pack(side="top", fill="x")
        self.mainframe = Frame(self.window)
        self.mainframe.pack(expand=True, fill="both")
        self.bottmframe = Frame(self.window, height=GUI.bottomheight)
        self.bottomframe.pack(side="bottom", fill="x")
