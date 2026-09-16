def copy_selection_access_string(self):
    selection = self.get_selection()
    if not selection:
        cursor = self.grid.actions.cursor
        selection = Selection([], [], [], [], [tuple(cursor[:2])])
    shape = self.grid.code_array.shape
    tab = self.grid.current_table
    access_string = selection.get_access_string(shape, tab)
    self.grid.main_window.clipboard.set_clipboard(access_string)
    statustext = _('Cell reference copied to clipboard: {access_string}')
    statustext = statustext.format(access_string=access_string)
    post_command_event(self.main_window, self.StatusBarMsg, text=statustext)