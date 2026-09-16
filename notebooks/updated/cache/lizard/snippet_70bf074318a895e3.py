def execute_dialog(self, title):
    msg_dlg = self.create_message_dialog(title)
    msg_dlg.run()
    msg_dlg.destroy()
    return