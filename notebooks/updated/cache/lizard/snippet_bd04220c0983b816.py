def move(self, item, parent, index):
    self._visual_drag.move(item, parent, index)
    ttk.Treeview.move(self, item, parent, index)