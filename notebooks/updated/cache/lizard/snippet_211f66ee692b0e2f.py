def _update_view(self, p_data):
    view = self._viewdata_to_view(p_data)
    if self.column_mode == _APPEND_COLUMN or self.column_mode == _COPY_COLUMN:
        self._add_column(view)
    elif self.column_mode == _INSERT_COLUMN:
        self._add_column(view, self.columns.focus_position)
    elif self.column_mode == _EDIT_COLUMN:
        current_column = self.columns.focus
        current_column.title = p_data['title']
        current_column.view = view
    self._viewwidget_visible = False
    self._blur_commandline()