def to_json(self, skip_nulls=True):
    return json.dumps(self.to_dict(skip_nulls=skip_nulls))