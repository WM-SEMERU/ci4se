def set_authoring_nodes(self, editor):
    project_node = self.default_project_node
    file_node = self.register_file(editor.file, project_node)
    editor_node = self.register_editor(editor, file_node)
    return True