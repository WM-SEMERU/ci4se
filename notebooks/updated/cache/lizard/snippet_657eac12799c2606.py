def model_changed(self, model, prop_name, info):
    current_enables = self._get_config_enables()
    if not self._enables == current_enables:
        filtered_buffer_update_needed = True
        if all(self._enables[key] == current_enables[key] for key in [
            'VERBOSE', 'DEBUG', 'INFO', 'WARNING', 'ERROR']):
            follow_mode_key = 'CONSOLE_FOLLOW_LOGGING'
            only_follow_mode_changed = self._enables[follow_mode_key
                ] != current_enables[follow_mode_key]
            filtered_buffer_update_needed = not only_follow_mode_changed
        self._enables = current_enables
        self.view.set_enables(self._enables)
        if filtered_buffer_update_needed:
            self.update_filtered_buffer()
        else:
            self.view.scroll_to_cursor_onscreen()