def open_window(self, widget, data=None):
    if data is not None:
        self.kwargs = data.get('kwargs', None)
        self.top_assistant = data.get('top_assistant', None)
        self.current_main_assistant = data.get('current_main_assistant', None)
        self.debugging = data.get('debugging', False)
        if not self.debugging:
            self.debug_btn.set_label('Debug logs')
        else:
            self.debug_btn.set_label('Info logs')
    self.store.clear()
    self.debug_logs = dict()
    self.debug_logs['logs'] = list()
    self.thread = threading.Thread(target=self.dev_assistant_start)
    project_name = self.parent.path_window.get_data()[1]
    if self.kwargs.get('github'):
        self.link = self.gui_helper.create_link_button(
            'Link to project on Github', 'http://www.github.com/{0}/{1}'.
            format(self.kwargs.get('github'), project_name))
        self.link.set_border_width(6)
        self.link.set_sensitive(False)
        self.info_box.pack_start(self.link, False, False, 12)
    self.run_list_view.connect('size-allocate', self.list_view_changed)
    os.chdir(os.path.expanduser('~'))
    self.run_window.show_all()
    self.disable_buttons()
    self.thread.start()