def get_relation_cols(self):
    retlst = []
    for flt, value in zip(self.filters, self.values):
        if isinstance(flt, FilterRelation) and value:
            retlst.append(flt.column_name)
    return retlst