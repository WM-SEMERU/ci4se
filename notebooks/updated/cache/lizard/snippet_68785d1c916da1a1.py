def get_features(self, yam):
    mcap = [c for c in self.capabilities if c.parameters.get('module', None
        ) == yam][0]
    if not mcap.parameters.get('features'):
        return []
    return mcap.parameters['features'].split(',')