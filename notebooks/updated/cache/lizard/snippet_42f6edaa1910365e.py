def show_event_analysis_dialog(self):
    self.event_analysis_dialog.update_types()
    self.event_analysis_dialog.update_groups()
    self.event_analysis_dialog.update_cycles()
    self.event_analysis_dialog.show()