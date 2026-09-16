def setup_columns(self):
    tv = self.view['tv_categories']
    tv.set_model(self.model)
    cell = gtk.CellRendererText()
    tvcol = gtk.TreeViewColumn('Name', cell)

    def cell_data_func(col, cell, mod, it):
        if mod[it][0]:
            cell.set_property('text', mod[it][0].name)
        return
    tvcol.set_cell_data_func(cell, cell_data_func)
    tv.append_column(tvcol)
    return