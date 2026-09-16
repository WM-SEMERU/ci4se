def _create_notebook_page(self, assistant):
    grid_lang = self.gui_helper.create_gtk_grid()
    scrolled_window = self.gui_helper.create_scrolled_window(grid_lang)
    row = 0
    column = 0
    scrolled_window.main_assistant, sub_as = assistant.get_subassistant_tree()
    for ass in sorted(sub_as, key=lambda x: x[0].fullname.lower()):
        if column > 2:
            row += 1
            column = 0
        if not ass[1]:
            self.gui_helper.add_button(grid_lang, ass, row, column)
        else:
            self.gui_helper.add_submenu(grid_lang, ass, row, column)
        column += 1
    if column > 2:
        row += 1
        column = 0
    self.gui_helper.add_install_button(grid_lang, row, column)
    column += 1
    if row == 0 and len(sub_as) < 3:
        while column < 3:
            btn = self.gui_helper.create_button(style=Gtk.ReliefStyle.NONE)
            btn.set_sensitive(False)
            btn.hide()
            grid_lang.attach(btn, column, row, 1, 1)
            column += 1
    return scrolled_window