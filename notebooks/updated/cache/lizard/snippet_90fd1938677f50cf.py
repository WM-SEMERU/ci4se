def primary_measures(self):
    from ambry.valuetype.core import ROLE
    for c in self.columns:
        if not c.parent and c.role == ROLE.MEASURE:
            yield c