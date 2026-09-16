def map(self, mapper):
    if isinstance(mapper, ABCSeries):
        mapper = mapper.to_dict()
    if isinstance(mapper, abc.Mapping):
        fill_value = mapper.get(self.fill_value, self.fill_value)
        sp_values = [mapper.get(x, None) for x in self.sp_values]
    else:
        fill_value = mapper(self.fill_value)
        sp_values = [mapper(x) for x in self.sp_values]
    return type(self)(sp_values, sparse_index=self.sp_index, fill_value=
        fill_value)