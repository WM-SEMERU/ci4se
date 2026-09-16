def to_dict(self):
    return {'schema': self.schema, 'name': self.name, 'columns': [col.
        to_dict() for col in self._columns], 'foreign_keys': self.
        foreign_keys.to_dict(), 'ref_keys': self.ref_keys.to_dict()}