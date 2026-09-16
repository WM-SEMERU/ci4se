def search_by_name(cls, query, name):
    query = query.filter(db.or_(cls.first_name.contains(name), cls.
        last_name.contains(name)))
    return query