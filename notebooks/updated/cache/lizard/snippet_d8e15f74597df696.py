def current_dim_changed(self, index):
    self.last_dim = index
    string_size = ['%i'] * 3
    string_size[index] = '<font color=red>%i</font>'
    self.shape_label.setText(('Shape: (' + ', '.join(string_size) + ')    '
        ) % self.data.shape)
    if self.index_spin.value() != 0:
        self.index_spin.setValue(0)
    else:
        self.change_active_widget(0)
    self.index_spin.setRange(-self.data.shape[index], self.data.shape[index
        ] - 1)