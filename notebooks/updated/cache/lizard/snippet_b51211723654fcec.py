def save_file_dialog(wildcard):
    app = wx.App(None)
    dialog = wx.FileDialog(None, 'Save file as ...', defaultDir=os.getcwd(),
        defaultFile='', wildcard=wildcard, style=wx.SAVE)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
        print('You chose the following filename: %s' % path)
    else:
        path = None
    dialog.Destroy()
    return path