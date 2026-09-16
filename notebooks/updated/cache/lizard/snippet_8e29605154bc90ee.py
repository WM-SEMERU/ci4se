def select_entry(self, core_element_id, by_cursor=True):
    for row_num, element_row in enumerate(self.list_store):
        if element_row[self.ID_STORAGE_ID] == core_element_id:
            if by_cursor:
                self.tree_view.set_cursor(row_num)
            else:
                self.tree_view.get_selection().select_path((row_num,))
            break