def apply_clicked(self, button):
    if isinstance(self.model.state, LibraryState):
        return
    self.set_script_text(self.view.get_text())