def build(self, builder):
    params = dict(OID=self.oid, Name=self.name)
    if self.location_type:
        params.update(dict(LocationType=self.location_type.value))
    self.mixin()
    self.mixin_params(params)
    builder.start('Location', params)
    for mdv in self.metadata_versions:
        mdv.build(builder)
    builder.end('Location')