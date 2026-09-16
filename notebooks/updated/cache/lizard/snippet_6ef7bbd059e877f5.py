def update_notes(self, xml_file, new=False):
    if new:
        create_empty_annotations(xml_file, self.parent.info.dataset)
        self.annot = Annotations(xml_file)
    else:
        self.annot = Annotations(xml_file)
    self.enable_events()
    self.parent.create_menubar()
    self.idx_stage.clear()
    for one_stage in STAGE_NAME:
        self.idx_stage.addItem(one_stage)
    self.idx_stage.setCurrentIndex(-1)
    self.idx_quality.clear()
    for one_qual in QUALIFIERS:
        self.idx_quality.addItem(one_qual)
    self.idx_quality.setCurrentIndex(-1)
    w1 = self.idx_summary.takeAt(1).widget()
    w2 = self.idx_summary.takeAt(1).widget()
    self.idx_summary.removeWidget(w1)
    self.idx_summary.removeWidget(w2)
    w1.deleteLater()
    w2.deleteLater()
    b1 = QGroupBox('Staging')
    layout = QFormLayout()
    for one_stage in STAGE_NAME:
        layout.addRow(one_stage, QLabel(''))
    b1.setLayout(layout)
    self.idx_summary.addWidget(b1)
    self.idx_stage_stats = layout
    b2 = QGroupBox('Signal quality')
    layout = QFormLayout()
    for one_qual in QUALIFIERS:
        layout.addRow(one_qual, QLabel(''))
    b2.setLayout(layout)
    self.idx_summary.addWidget(b2)
    self.idx_qual_stats = layout
    self.display_notes()