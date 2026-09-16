def go_to_line(self):
    editor = self.get_current_editor()
    if not editor:
        return False
    line, state = QInputDialog.getInt(self, 'Goto Line Number',
        'Line number:', min=1)
    if not state:
        return False
    LOGGER.debug("> Chosen line number: '{0}'.".format(line))
    return editor.go_to_line(line)