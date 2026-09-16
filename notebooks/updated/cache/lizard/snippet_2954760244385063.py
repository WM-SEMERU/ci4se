def on_install(self, editor):
    super(FoldingPanel, self).on_install(editor)
    self.context_menu = QtWidgets.QMenu(_('Folding'), self.editor)
    action = self.action_collapse = QtWidgets.QAction(_('Collapse'), self.
        context_menu)
    action.setShortcut('Shift+-')
    action.triggered.connect(self._on_action_toggle)
    self.context_menu.addAction(action)
    action = self.action_expand = QtWidgets.QAction(_('Expand'), self.
        context_menu)
    action.setShortcut('Shift++')
    action.triggered.connect(self._on_action_toggle)
    self.context_menu.addAction(action)
    self.context_menu.addSeparator()
    action = self.action_collapse_all = QtWidgets.QAction(_('Collapse all'),
        self.context_menu)
    action.setShortcut('Ctrl+Shift+-')
    action.triggered.connect(self._on_action_collapse_all_triggered)
    self.context_menu.addAction(action)
    action = self.action_expand_all = QtWidgets.QAction(_('Expand all'),
        self.context_menu)
    action.setShortcut('Ctrl+Shift++')
    action.triggered.connect(self._on_action_expand_all_triggered)
    self.context_menu.addAction(action)
    self.editor.add_menu(self.context_menu)