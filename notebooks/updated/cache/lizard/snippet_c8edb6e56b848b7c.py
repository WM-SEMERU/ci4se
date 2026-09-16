def paste_action_callback(self, *event):
    if react_to_event(self.view, self.tree_view, event
        ) and self.active_entry_widget is None:
        _, dict_paths = self.get_view_selection()
        selected_data_list = (rafcon.gui.clipboard.global_clipboard.
            get_semantic_dictionary_list())
        if not dict_paths and not self.model.state.semantic_data:
            dict_paths = [[]]
        for target_dict_path_as_list in dict_paths:
            prev_value = self.model.state.semantic_data
            value = self.model.state.semantic_data
            for path_element in target_dict_path_as_list:
                prev_value = value
                value = value[path_element]
            if not isinstance(value, dict) and len(dict_paths) <= 1:
                target_dict_path_as_list.pop(-1)
                value = prev_value
            if isinstance(value, dict):
                for key_to_paste, value_to_add in selected_data_list:
                    self.model.state.add_semantic_data(target_dict_path_as_list
                        , value_to_add, key_to_paste)
        self.reload_tree_store_data()