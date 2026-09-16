def add_channels_to_list(self, l, add_ref=False):
    l.clear()
    l.setSelectionMode(QAbstractItemView.ExtendedSelection)
    for chan in self.chan_name:
        item = QListWidgetItem(chan)
        l.addItem(item)
    if add_ref:
        item = QListWidgetItem('_REF')
        l.addItem(item)