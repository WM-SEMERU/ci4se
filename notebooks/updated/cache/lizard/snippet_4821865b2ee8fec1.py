def where(self, *custom_restrictions, **restrictions):
    for attr, value in restrictions.items():
        self.where_query[attr] = value
    if custom_restrictions:
        self.custom_where.append(tuple(custom_restrictions))
    return self