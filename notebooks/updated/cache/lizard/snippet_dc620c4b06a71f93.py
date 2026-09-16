def update_actions(self):
    self.clear()
    self.recent_files_actions[:] = []
    for file in self.manager.get_recent_files():
        action = QtWidgets.QAction(self)
        action.setText(os.path.split(file)[1])
        action.setToolTip(file)
        action.setStatusTip(file)
        action.setData(file)
        action.setIcon(self.icon_provider.icon(QtCore.QFileInfo(file)))
        action.triggered.connect(self._on_action_triggered)
        self.addAction(action)
        self.recent_files_actions.append(action)
    self.addSeparator()
    action_clear = QtWidgets.QAction(_('Clear list'), self)
    action_clear.triggered.connect(self.clear_recent_files)
    if isinstance(self.clear_icon, QtGui.QIcon):
        action_clear.setIcon(self.clear_icon)
    elif self.clear_icon:
        theme = ''
        if len(self.clear_icon) == 2:
            theme, path = self.clear_icon
        else:
            path = self.clear_icon
        icons.icon(theme, path, 'fa.times-circle')
    self.addAction(action_clear)