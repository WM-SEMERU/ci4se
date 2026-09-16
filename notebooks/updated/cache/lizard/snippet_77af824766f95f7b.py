def add(cls, zone_id, version_id, record):
    return cls.call('domain.zone.record.add', zone_id, version_id, record)