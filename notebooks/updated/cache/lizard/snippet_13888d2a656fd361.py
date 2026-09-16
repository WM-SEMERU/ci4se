def undock_sidebar(self, window_key, widget=None, event=None):
    undocked_window_name = window_key.lower() + '_window'
    widget_name = window_key.lower()
    undocked_window_view = getattr(self.view, undocked_window_name)
    undocked_window = undocked_window_view.get_top_widget()
    if os.getenv('RAFCON_START_MINIMIZED', False):
        undocked_window.iconify()
    gui_helper_label.set_window_size_and_position(undocked_window, window_key)
    self.view[widget_name].reparent(undocked_window_view['central_eventbox'])
    self.view['undock_{}_button'.format(widget_name)].hide()
    getattr(self, 'on_{}_hide_clicked'.format(widget_name))(None)
    self.view['{}_return_button'.format(widget_name)].hide()
    main_window = self.view.get_top_widget()
    state_handler = main_window.connect('window-state-event', self.
        undock_window_callback, undocked_window)
    self.handler_ids[undocked_window_name] = {'state': state_handler}
    undocked_window.set_transient_for(main_window)
    main_window.grab_focus()
    global_runtime_config.set_config_value(window_key + '_WINDOW_UNDOCKED',
        True)