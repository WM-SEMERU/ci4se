def on_summary_menu_close(self, update):
    logging.info('closing summary_menu menu, update=%s', update)
    if update:
        for sensor, visible_sensors in self.summary_menu.active_sensors.items(
            ):
            self.visible_summaries[sensor].update_visibility(visible_sensors)
    self.main_window_w.base_widget[0].body[self.summary_widget_index
        ] = self._generate_summaries()
    self.original_widget = self.main_window_w