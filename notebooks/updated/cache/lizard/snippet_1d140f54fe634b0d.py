def _update_gui_text_tabs(self):
    for index, page in enumerate(self.pages):
        self.tabWidget.setTabText(index, '{} (Alt+&{}){}'.format(page.
            text_tab, index + 1, ' (changed)' if page.flag_changed else ''))