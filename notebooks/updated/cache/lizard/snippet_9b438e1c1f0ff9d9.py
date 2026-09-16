def measures(self):
    from ambry.valuetype.core import ROLE
    return [c for c in self.columns if c.role == ROLE.MEASURE]