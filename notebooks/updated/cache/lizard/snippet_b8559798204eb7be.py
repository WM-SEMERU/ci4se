def cql_encode_sequence(self, val):
    return '(%s)' % ', '.join(self.mapping.get(type(v), self.
        cql_encode_object)(v) for v in val)