def get_rollout_from_id(self, rollout_id):
    layer = self.rollout_id_map.get(rollout_id)
    if layer:
        return layer
    self.logger.error('Rollout with ID "%s" is not in datafile.' % rollout_id)
    return None