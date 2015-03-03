# -*- coding: cp936 -*-

'重定向'
import wx
    
class Frame(wx.Frame):
    def __init__(self,parent,id,title):
        print "Frame __init__"
        wx.Frame.__init__(self,parent,id,title)
class App(wx.App):
    def __init__(self,redirect=True,filename=None):
        print 'App init'
        wx.App.__init__(self,redirect,filename)
    def OnInit(self):
        print 'OnInit'
        self.frame=Frame(None,-1,'Startup')
        self.frame.Show()
        self.SetTopWindow(self.frame)
       # print>>sys.stderr,"A pretend error message"
        return True
    def OnExit(self):
        print 'OnExit'
if __name__=='__main__':
    app=App(redirect=True)
    print 'before MainLoop'
    app.MainLoop()
    print 'after app'
