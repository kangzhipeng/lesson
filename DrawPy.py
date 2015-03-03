# -*- coding: cp936 -*-
import wx
#按钮属性页面
class dataButton(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,None,id,'属性',size=(300,300))
        pannel=wx.Panel(self)
        cbutton=self.creatButton(pannel,'NewBuaa',self.onButton,pos=(0,0))
    def onButton(self,event):
        pass
    def creatButton(self,parnet,label,handler,size=(100,20),pos=(0,0)):
        button=wx.Button(parnet,-1,label,pos)
        self.Bind(wx.EVT_BUTTON,handler,button)
        return button
#画面主页面        
class NewPage(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'example',size=(500,600))
        panel=wx.Panel(self)
        statusBar = self.CreateStatusBar() #1 创建状态栏
        aButton=self.creatButton(panel,'NewBuaa',self.publicHandler,pos=(0,0))
        aText=self.creatStaticText(panel,'xxxxxxx',size=(490,90),pos=(5,40),name="a111")
        #box.Add(panel,0,wx.EXPAND)
        #box.Add(aButton,1,wx.EXPAND)
        #box.Add(bButton,2,wx.EXPAND)
        #self.SetSizer(box)
    def creatButton(self,parnet,label,handler,size=(100,20),pos=(0,0)):
        button=wx.Button(parnet,-1,label,pos)
        self.Bind(wx.EVT_BUTTON,handler,button)
        return button
    def creatStaticText(self,parent,label,pos=(0,80),size=(200,100),name="new"):
        text=wx.StaticText(parent,-1,label,pos,size,wx.ALIGN_CENTER,name)
        text.SetBackgroundColour('white')
        return text
    def publicHandler(self,event):
        app1=wx.App(True)
        frame=dataButton(self,id=-1)
        frame.Show()
        app1.MainLoop()
if __name__=='__main__':
    app=wx.App(True)
    frame=NewPage(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
