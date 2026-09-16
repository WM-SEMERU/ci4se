def make_menu(self):
    menu = wx.Menu()
    item = menu.Append(-1, 'Recent Searches')
    item.Enable(False)
    for __id, txt in enumerate(self.search_history):
        menu.Append(__id, txt)
    return menu