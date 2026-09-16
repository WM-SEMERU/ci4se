def change_frozen_attr(self):
    if self.grid.selection:
        statustext = _('Freezing selections is not supported.')
        post_command_event(self.main_window, self.StatusBarMsg, text=statustext
            )
    cursor = self.grid.actions.cursor
    frozen = self.grid.code_array.cell_attributes[cursor]['frozen']
    if frozen:
        self.grid.code_array.frozen_cache.pop(repr(cursor))
    else:
        res_obj = self.grid.code_array[cursor]
        self.grid.code_array.frozen_cache[repr(cursor)] = res_obj
    selection = Selection([], [], [], [], [cursor[:2]])
    self.set_attr('frozen', not frozen, selection=selection)