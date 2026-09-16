def add_buttons(self, classification):
    if self.layer_mode == layer_mode_continuous['key']:
        self.restore_default_button = QPushButton(tr('Restore Default'))
        self.restore_default_button.clicked.connect(partial(self.
            restore_default_button_clicked, classification=classification))
    self.save_button = QPushButton(tr('Save'))
    self.save_button.clicked.connect(partial(self.save_button_clicked,
        classification=classification))
    button_layout = QHBoxLayout()
    button_layout.addStretch(1)
    button_layout.addWidget(self.restore_default_button)
    button_layout.addWidget(self.save_button)
    button_layout.setStretch(0, 3)
    button_layout.setStretch(1, 1)
    button_layout.setStretch(2, 1)
    self.right_layout.addLayout(button_layout)