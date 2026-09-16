def OnTextColor(self, event):
    color = event.GetValue().GetRGB()
    post_command_event(self, self.TextColorMsg, color=color)