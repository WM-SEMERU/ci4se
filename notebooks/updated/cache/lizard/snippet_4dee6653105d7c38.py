def close_others(self):
    current_widget = self.currentWidget()
    self._try_close_dirty_tabs(exept=current_widget)
    i = 0
    while self.count() > 1:
        widget = self.widget(i)
        if widget != current_widget:
            self.removeTab(i)
        else:
            i = 1