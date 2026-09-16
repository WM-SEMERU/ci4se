def handle(self, data, **kwargs):
    if self.many:
        return self.mapper.many(raw=self.raw, **self.mapper_kwargs).serialize(
            data, role=self.role)
    else:
        return self.mapper(obj=data, raw=self.raw, **self.mapper_kwargs
            ).serialize(role=self.role)