def find_editor_tab(self, file):
    for i in range(self.Script_Editor_tabWidget.count()):
        if not self.get_widget(i).file == file:
            continue
        LOGGER.debug("> File '{0}': Tab index '{1}'.".format(file, i))
        return i