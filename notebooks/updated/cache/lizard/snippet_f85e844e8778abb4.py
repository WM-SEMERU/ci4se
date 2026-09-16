def set_editor_lock(self, locked=True):
    self.view['new_entry'].set_sensitive(not locked)
    self.view['new_dict_entry'].set_sensitive(not locked)
    self.view['delete_entry'].set_sensitive(not locked)
    for current_column in self.view['semantic_data_tree_view'].get_columns():
        current_column.get_cells()[0].set_property('editable', not locked)