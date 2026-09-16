def get_links_of_type(self, s_type=''):
    satellites = {'arbiter': getattr(self, 'arbiters', []), 'scheduler':
        getattr(self, 'schedulers', []), 'broker': getattr(self, 'brokers',
        []), 'poller': getattr(self, 'pollers', []), 'reactionner': getattr
        (self, 'reactionners', []), 'receiver': getattr(self, 'receivers', [])}
    if not s_type:
        result = {}
        for sat_type in satellites:
            for sat_uuid in satellites[sat_type]:
                result[sat_uuid] = satellites[sat_type][sat_uuid]
        return result
    if s_type in satellites:
        return satellites[s_type]
    return None