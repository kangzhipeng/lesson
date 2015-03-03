import wx
import wx.grid
import GenericTable

data=(('Bob','Dernier'),('Ry','Sa'),('Gary','Math'),('Le','Dur'),('k','y'),
      ('r','c'),('cc','dd'),('de','eee'),('qa','sw')
    )
colLabels=('Last','Frist')
rowLabels=('A','B','C','D','E','F','G','H','I')
class simpleGrid(wx.grid.Grid):
    def __init__(self,parent):
       wx.grid.Grid.__init__(self,parent,-1)
       tableBase=GenericTable.GenericTable(data,rowLabels,colLabels)
       self.SetTable(tableBase)
class testFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,-1,'A Grid',size=(300,400))
        grid=simpleGrid(self)

if __name__=='__main__':
    app=wx.App(True)
    frame=testFrame(None)
    frame.Show()
    app.MainLoop()
    
