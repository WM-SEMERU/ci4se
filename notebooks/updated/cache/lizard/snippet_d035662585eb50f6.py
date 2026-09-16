def aggregate_hazard_preparation(self):
    LOGGER.info('ANALYSIS : Aggregate hazard preparation')
    self.set_state_process('hazard', 'Make hazard layer valid')
    self.hazard = clean_layer(self.hazard)
    self.debug_layer(self.hazard)
    self.set_state_process('aggregation',
        'Union hazard polygons with aggregation areas and assign hazard class')
    self._aggregate_hazard_impacted = union(self.hazard, self.aggregation)
    self.debug_layer(self._aggregate_hazard_impacted)