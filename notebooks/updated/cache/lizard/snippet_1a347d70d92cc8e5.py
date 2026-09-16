def add_context_action(self, action):
    self.main_tab_widget.context_actions.append(action)
    for child_splitter in self.child_splitters:
        child_splitter.add_context_action(action)