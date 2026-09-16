def OnLineWidth(self, event):
    linewidth_combobox = event.GetEventObject()
    idx = event.GetInt()
    width = int(linewidth_combobox.GetString(idx))
    borders = self.bordermap[self.borderstate]
    post_command_event(self, self.BorderWidthMsg, width=width, borders=borders)