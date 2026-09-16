def run_cell(self):
    text, line = self.get_current_editor().get_cell_as_executable_code()
    self._run_cell_text(text, line)