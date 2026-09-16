def get_by_id(cls, record_id, execute=True):
    query = cls.base_query().where(cls.id == record_id)
    if execute:
        return query.get()
    return query