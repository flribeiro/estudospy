import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Alo Mundo", size=(320,240))
frame.Show(True)

app.MainLoop()
