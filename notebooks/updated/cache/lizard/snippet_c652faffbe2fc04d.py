def load_file(self, filename):
    self.tree_editor.load_file(filename)
    self.project_name.configure(text=filename)
    self.currentfile = filename
    self.is_changed = False