def to_dict(self, db_obj):
    return {'_id': db_obj.identifier, 'timestamp': str(db_obj.timestamp.
        isoformat()), 'properties': db_obj.properties}