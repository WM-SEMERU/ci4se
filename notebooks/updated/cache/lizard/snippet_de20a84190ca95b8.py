def update_views(self):
    super(Plugin, self).update_views()
    for key in iterkeys(self.stats):
        self.views[key]['optional'] = True