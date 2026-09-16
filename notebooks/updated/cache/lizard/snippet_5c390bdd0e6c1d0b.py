def set_current_state(self):
    if not self.thresholds:
        self.thresholds = self.parent.get_existing_keyword('thresholds')
    if not self.value_maps:
        self.value_maps = self.parent.get_existing_keyword('value_maps')