def set_alpha_for_selection(self, alpha):
    selection = self.treeview_layers.get_selection()
    list_store, selected_iter = selection.get_selected()
    if selected_iter is None:
        return
    else:
        surface_name, original_alpha = list_store[selected_iter]
        self.set_alpha(surface_name, alpha)
        self.set_scale_alpha_from_selection()