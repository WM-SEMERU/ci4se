def click_event(self, event):
    self.prevent_refresh = False
    try:
        if self.error_messages:
            button = event['button']
            if button == 1:
                self.error_index = (self.error_index + 1) % len(self.
                    error_messages)
                error = self.error_messages[self.error_index]
                self.error_output(error)
            if button == 3:
                self.hide_errors()
            if button != 2 or (self.terminated or self.disabled):
                self.prevent_refresh = True
        elif self.click_events:
            click_method = getattr(self.module_class, 'on_click')
            if self.click_events == self.PARAMS_NEW:
                click_method(event)
            else:
                click_method(self.i3status_thread.json_list, self.config[
                    'py3_config']['general'], event)
            self.set_updated()
        else:
            self.prevent_refresh = True
    except Exception:
        msg = 'on_click event in `{}` failed'.format(self.module_full_name)
        self._py3_wrapper.report_exception(msg)