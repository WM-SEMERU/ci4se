def focus_notebook_page_of_controller(self, controller):
    if controller not in self.get_child_controllers():
        return
    if not self.modification_history_was_focused and isinstance(controller,
        ModificationHistoryTreeController) and self.view is not None:
        self.view.bring_tab_to_the_top('history')
        self.modification_history_was_focused = True
    if self.view is not None and isinstance(controller,
        ExecutionHistoryTreeController):
        self.view.bring_tab_to_the_top('execution_history')
        self.modification_history_was_focused = False