def build(self, builder):
    params = dict(OID=self.oid, Name=self.name)
    if self.unit_dictionary_name:
        params['mdsol:UnitDictionaryName'] = self.unit_dictionary_name
    for suffix in ['A', 'B', 'C', 'K']:
        val = getattr(self, 'constant_{0}'.format(suffix.lower()))
        params['mdsol:Constant{0}'.format(suffix)] = str(val)
    if self.standard_unit:
        params['mdsol:StandardUnit'] = 'Yes'
    builder.start('MeasurementUnit', params)
    for child in self.symbols:
        child.build(builder)
    builder.end('MeasurementUnit')