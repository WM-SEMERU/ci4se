def main_btn_clicked(self, widget, data=None):
    self.remove_link_button()
    data = dict()
    data['debugging'] = self.debugging
    self.run_window.hide()
    self.parent.open_window(widget, data)