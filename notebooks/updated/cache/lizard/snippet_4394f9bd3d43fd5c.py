def update(self):
    self.filename = self.parent.info.dataset.filename
    self.chan = self.parent.info.dataset.header['chan_name']
    for chan in self.chan:
        self.idx_chan.addItem(chan)