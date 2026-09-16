def start_editing(self, treeview, event):
    x, y = int(event.x), int(event.y)
    ret = treeview.get_path_at_pos(x, y)
    if not ret:
        return False
    path, column, cellx, celly = ret
    treeview.row_activated(path, Gtk.TreeViewColumn(None))
    treeview.set_cursor(path)
    return False