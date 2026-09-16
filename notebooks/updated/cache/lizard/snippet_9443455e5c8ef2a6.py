def setup_ui(self):
    w = QtGui.QWidget(self)
    w.setLayout(self.central_vbox)
    self.setCentralWidget(w)
    releasetypes = [djadapter.RELEASETYPES['work'], djadapter.RELEASETYPES[
        'release'], djadapter.RELEASETYPES['handoff']]
    self.browser = FileBrowser(self._filetype, releasetypes, self.
        get_current_file, self)
    self.central_vbox.insertWidget(0, self.browser)
    self.asset_comment_pte = self.create_comment_edit()
    self.browser.asset_vbox.addWidget(self.asset_open_pb)
    self.asset_new_hbox = QtGui.QHBoxLayout()
    self.asset_new_hbox.addWidget(self.asset_save_pb)
    self.asset_new_hbox.addWidget(self.asset_descriptor_lb)
    self.asset_new_hbox.addWidget(self.asset_descriptor_le)
    self.browser.asset_vbox.addLayout(self.asset_new_hbox)
    self.browser.asset_vbox.addWidget(self.asset_comment_pte)
    self.shot_comment_pte = self.create_comment_edit()
    self.browser.shot_vbox.addWidget(self.shot_open_pb)
    self.shot_new_hbox = QtGui.QHBoxLayout()
    self.shot_new_hbox.addWidget(self.shot_save_pb)
    self.shot_new_hbox.addWidget(self.shot_descriptor_lb)
    self.shot_new_hbox.addWidget(self.shot_descriptor_le)
    self.browser.shot_vbox.addLayout(self.shot_new_hbox)
    self.browser.shot_vbox.addWidget(self.shot_comment_pte)
    ph = 'Enter New Descriptor'
    self.asset_descriptor_le.setPlaceholderText(ph)
    self.shot_descriptor_le.setPlaceholderText(ph)
    self.setup_icons()