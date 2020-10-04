import wx
import wx.adv
import os
import time
import multiprocessing

from Models.getMetadata import getMetadata, getData
from Models.getWindows import checkExsit
from Models.presence import connectPresence, updatePresence, stopPresence

processOnline = False

class MyTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = "logo.ico"
    ID_EXIT = wx.NewId()
    ID_SHOW_WEB = wx.NewId()
    TITLE = "Haroku"

    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)
        self.Bind(wx.EVT_MENU, self.onExit, id=self.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.onShowWeb, id=self.ID_SHOW_WEB)

    def onExit(self, event):
        wx.Exit()

    def onShowWeb(self, event):
        pass

    def CreatePopupMenu(self):
        menu = wx.Menu()
        for mentAttr in self.getMenuAttrs():
            menu.Append(mentAttr[1], mentAttr[0])
        return menu

    def getMenuAttrs(self):
        return [('Run presence', self.ID_SHOW_WEB),
                ('Exit', self.ID_EXIT)]

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self)
        MyTaskBarIcon()

class MyApp(wx.App):
    def OnInit(self):
        MyFrame()
        return True

def Main():
    global processOnline
    while True:
        processName_list, processName_dict = getMetadata()
        if processOnline == False:
            for processName in processName_list:
                processOnline = checkExsit(processName)
                if processOnline == True:
                    clientId, state, details, large_image, large_text, small_image, small_text = getData(processName_dict[processName])
                    RPC = updatePresence(
                        clientId,
                        state = state,
                        details = details,
                        large_image = large_image,
                        large_text = large_text,
                        small_image = small_image,
                        small_text = small_text,
                        start = time.time()
                        )
                    while processOnline == True:
                        processOnline = checkExsit(processName)
                        if processOnline == False:
                            RPC.clear()
                        time.sleep(5)
        time.sleep(3)


if __name__ == "__main__":
    mp = multiprocessing.Process (target = Main)
    mp.start ()
    app = MyApp()
    app.MainLoop()