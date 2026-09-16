def restore_geometry_state(self, gs):
    if not gs:
        return
    if gs.get('geometry', None):
        self.restoreGeometry(gs['geometry'])
    if gs.get('state', None):
        self.restoreState(gs['state'])