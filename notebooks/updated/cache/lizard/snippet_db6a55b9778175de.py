def recommend(self, client_data, limit, extra_data={}):
    guids = self._curated_wl.get_randomized_guid_sample(limit)
    results = [(guid, 1.0) for guid in guids]
    log_data = client_data['client_id'], str(guids)
    self.logger.info('Curated recommendations client_id: [%s], guids: [%s]' %
        log_data)
    return results