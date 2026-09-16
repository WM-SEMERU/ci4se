def __set_authoring_nodes(self, source, target):
    editor = self.__script_editor.get_editor(source)
    editor.set_file(target)
    self.__script_editor.model.update_authoring_nodes(editor)