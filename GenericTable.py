
#GenericTable GUI_Learn5-3

import wx
import wx.grid

class GenericTable(wx.grid.PyGridTableBase):
    def __init__(self,data,rowLabels=None,colLabels=None):
        wx.grid.PyGridTableBase.__init__(self)
        self.data=data
        self.rowlabels=rowLabels
        self.colLabels=colLabels

    def GetNumberRows(self):
        return len(self.data)
    def GetNumberCols(self):
        return len(self.data[0])
    def GetRowsLabel(self,row):
        if self.rowlabels:
            return self.rowlabels[row]
    def GetColsLabel(self,col):
         if self.collabels:
             return self.collabels[col]
                
    def GetValue(self,row,col):
        return self.data[row][col]
    def SetValue(self,row,col,value):
        pass
if __name__=='__main__':
    app=wx.App(True)
    frame= GenericTable(None)
    frame.show
    app.MainLoop()
