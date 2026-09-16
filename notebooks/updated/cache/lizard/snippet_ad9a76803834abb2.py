def add_widget(self, w):
    if self.layout():
        self.layout().addWidget(w)
    else:
        layout = QVBoxLayout(self)
        layout.addWidget(w)