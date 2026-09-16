def _update_proxy(self, change):
    if change['name'] in ['row', 'column']:
        super(AbstractWidgetItem, self)._update_proxy(change)
    else:
        self.proxy.data_changed(change)