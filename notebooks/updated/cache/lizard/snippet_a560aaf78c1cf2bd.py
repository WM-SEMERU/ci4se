def onContinue(self, event, grid, next_dia=None):
    if self.grid_frame.drop_down_menu:
        self.grid_frame.drop_down_menu.clean_up()
    grid.remove_starred_labels()
    grid.SaveEditControlValue()
    grid_name = str(grid.GetName())
    self.grid_frame.grid_builder.save_grid_data()
    validation_errors = self.validate(grid)
    if validation_errors:
        warn_string = ''
        for error_name, error_cols in list(validation_errors.items()):
            if error_cols:
                warn_string += 'You have {}: {}.\n\n'.format(error_name,
                    ', '.join(error_cols))
        warn_string += 'Are you sure you want to continue?'
        result = pw.warning_with_override(warn_string)
        if result == wx.ID_YES:
            pass
        else:
            return False
    else:
        wx.MessageBox('Saved!', 'Info', style=wx.OK | wx.ICON_INFORMATION)
    self.panel.Destroy()
    if next_dia:
        next_dia()
    else:
        self.contribution.propagate_lithology_cols()
        wx.MessageBox('Done!', 'Info', style=wx.OK | wx.ICON_INFORMATION)