def button_clicked(self, button):
    if button in (self.idx_ok, self.idx_apply):
        for i_config in range(self.stacked.count()):
            one_config = self.stacked.widget(i_config)
            if one_config.modified:
                lg.debug('Settings for ' + one_config.widget + ' were modified'
                    )
                one_config.get_values()
                if self.parent.info.dataset is not None:
                    one_config.update_widget()
                one_config.modified = False
        if button == self.idx_ok:
            self.accept()
    if button == self.idx_cancel:
        self.reject()