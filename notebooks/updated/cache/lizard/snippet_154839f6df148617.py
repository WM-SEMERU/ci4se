def update_views(self):
    super(Plugin, self).update_views()
    for key in ['cpu', 'mem', 'swap']:
        if key in self.stats:
            self.views[key]['decoration'] = self.get_alert(self.stats[key],
                header=key)