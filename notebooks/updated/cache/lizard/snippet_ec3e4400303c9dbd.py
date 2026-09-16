def _set_menu_toggles(self):
    toggles = [(self.main_toolbar, 'main_window_toolbar', _('Main toolbar')
        ), (self.macro_toolbar, 'macro_toolbar', _('Macro toolbar')), (self
        .macro_panel, 'macro_panel', _('Macro panel')), (self.
        attributes_toolbar, 'attributes_toolbar', _('Format toolbar')), (
        self.find_toolbar, 'find_toolbar', _('Find toolbar')), (self.
        widget_toolbar, 'widget_toolbar', _('Widget toolbar')), (self.
        entry_line_panel, 'entry_line_panel', _('Entry line')), (self.
        table_list_panel, 'table_list_panel', _('Table list'))]
    for toolbar, pane_name, toggle_label in toggles:
        pane = self._mgr.GetPane(pane_name)
        toggle_id = self.menubar.FindMenuItem(_('View'), toggle_label)
        if toggle_id != -1:
            toggle_item = self.menubar.FindItemById(toggle_id)
            toggle_item.Check(pane.IsShown())