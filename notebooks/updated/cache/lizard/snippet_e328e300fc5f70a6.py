def set_current_editor(self, file):
    index = self.find_editor_tab(file)
    if index is not None:
        self.Script_Editor_tabWidget.setCurrentIndex(index)
        return True