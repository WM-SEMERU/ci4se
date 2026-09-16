def load_config(self):
    expanded_state = self.get_option('expanded_state', None)
    if is_text_string(expanded_state):
        expanded_state = None
    if expanded_state is not None:
        self.explorer.treewidget.set_expanded_state(expanded_state)