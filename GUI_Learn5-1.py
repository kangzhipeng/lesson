
import wx
class myframe(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'example',size=(600,600))
        panel=wx.Panel(self,-1)
        self.createMenuBar()
        self.creatButtonBar(panel)
        self.creatTextField(panel)
    def menuData(self):
        return(("&File",
                ("&open","open in staus bar",self.OnOpen),
                ("&Quit","Quit",self.OnCloseWindow)),
               ("&Edit",
                ("&Copy","Copy",self.OnCopy)
                ),
               ("Option",
                ("&tolls","option",self.OnOption)),
               ("help",
                ("&help","helpp",self.OnHelp))

                )

    def buttonData(self):
        return(("Frist",self.OnFrist),
               ("<<PREV",self.OnPrev),
               ("Next>>",self.OnNext),
               ("Last",self.OnLast))
    def createMenuBar(self):
        menuBar=wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel=eachMenuData[0]
            menuItems=eachMenuData[1:]
            menuBar.Append(self.creatMenu(menuItems),menuLabel)
            self.SetMenuBar(menuBar)
    def creatMenu(self,MenuData):
        menu=wx.Menu()
        for eachlabel,eachStatus,eachHandler in MenuData:
            if not eachlabel:
                menu.AppendSepartor()
                continue
            menuItem=menu.Append(-1,eachlabel,eachStatus)
            self.Bind(wx.EVT_MENU,eachHandler,menuItem)
        return menu
    def creatButtonBar(self,parent,yPos=0):
        xPos=0
        for eachLabel,eachHandler,in self.buttonData():
            pos=(xPos,yPos)
            button=self.buildOneButton(parent,eachLabel,eachHandler,pos)
            xPos+=button.GetSize().width
    def buildOneButton(self,parent,label,handler,pos=(0,0)):
        button=wx.Button(parent,-1,label,pos)
        self.Bind(wx.EVT_BUTTON,handler,button)
        return button
    def textData(self) :
        return (("Frist Name",(10,50)),
                ("Last Name",(10,80)))
    def creatTextField(self,panel):
        for eachLabel,eachPos in self.textData():
            self.creatCaptionText(panel,eachLabel,eachPos)
    def creatCaptionText(self,panel,label,pos):
        static=wx.StaticText(panel,wx.NewId(),label,pos)
        textPos=(pos[0]+75,pos[1])
        wx.TextCtrl(panel,wx.NewId(),"",size=(100,-1),pos=textPos)
        
    def OnOpen(self):pass
    def OnCloseWindow(self):pass
    def OnCopy(self):pass
    def OnHelp(self):pass
    def OnFrist(self):pass
    def OnPrev(self):pass
    def OnNext(self):pass
    def OnLast(self):pass
    def OnOption(self):pass
    
if __name__=='__main__':
    app=wx.App(True)
    frame=myframe(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
    
