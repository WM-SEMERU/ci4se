def _run_cell_text(self, text, line):
    finfo = self.get_current_finfo()
    editor = self.get_current_editor()
    oe_data = editor.highlighter.get_outlineexplorer_data()
    try:
        cell_name = oe_data.get(line - 1).def_name
    except AttributeError:
        cell_name = ''
    if finfo.editor.is_python() and text:
        self.run_cell_in_ipyclient.emit(text, cell_name, finfo.filename,
            self.run_cell_copy)
    editor.setFocus()