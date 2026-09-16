def close_project(self):
    if self.current_active_project:
        self.switch_to_plugin()
        if self.main.editor is not None:
            self.set_project_filenames(self.main.editor.get_open_filenames())
        path = self.current_active_project.root_path
        self.current_active_project = None
        self.set_option('current_project_path', None)
        self.setup_menu_actions()
        self.sig_project_closed.emit(path)
        self.sig_pythonpath_changed.emit()
        if self.dockwidget is not None:
            self.set_option('visible_if_project_open', self.dockwidget.
                isVisible())
            self.dockwidget.close()
        self.explorer.clear()
        self.restart_consoles()