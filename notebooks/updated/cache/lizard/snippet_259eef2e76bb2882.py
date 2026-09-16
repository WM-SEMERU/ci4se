def save_fileAs(self):
    editor = self.get_current_editor()
    if not editor:
        return False
    file = umbra.ui.common.store_last_browsed_path(QFileDialog.
        getSaveFileName(self, 'Save As:', editor.file))
    if not file:
        return False
    candidate_editor = self.get_editor(file)
    if candidate_editor:
        if not candidate_editor is editor:
            raise foundations.exceptions.UserError(
                "{0} | '{1}' file is already opened!".format(self.__class__
                .__name__, file))
        else:
            return self.save_file(file)
    LOGGER.info("{0} | Saving '{1}' file!".format(self.__class__.__name__,
        file))
    self.__lock_editor(editor)
    self.unregister_node_path(editor)
    if editor.save_fileAs(file):
        self.__model.update_authoring_nodes(editor)
        language = self.__languages_model.get_file_language(file
            ) or self.__languages_model.get_language(self.__default_language)
        if editor.language.name != language.name:
            self.set_language(editor, language)
        return True