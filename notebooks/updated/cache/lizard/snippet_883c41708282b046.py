def toggle_help(self, event, mode=None):
    btn = self.toggle_help_btn
    shown = self.help_msg_boxsizer.GetStaticBox().IsShown()
    if mode == 'open':
        self.help_msg_boxsizer.ShowItems(True)
        btn.SetLabel('Hide help')
    elif mode == 'close':
        self.help_msg_boxsizer.ShowItems(False)
        btn.SetLabel('Show help')
    elif shown:
        self.help_msg_boxsizer.ShowItems(False)
        btn.SetLabel('Show help')
    else:
        self.help_msg_boxsizer.ShowItems(True)
        btn.SetLabel('Hide help')
    self.do_fit(None)