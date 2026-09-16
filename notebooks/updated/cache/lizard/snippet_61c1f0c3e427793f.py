def columns(self):
    try:
        r = self.expanded_url.resource.columns()
        return list(r)
    except AttributeError as e:
        pass
    return self.schema_columns