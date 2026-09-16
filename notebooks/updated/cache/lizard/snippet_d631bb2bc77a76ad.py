def validate(self, other):
    if other is None:
        return
    if other.table_type != self.table_type:
        raise TypeError(
            'incompatible table_type with existing [{other} - {self}]'.
            format(other=other.table_type, self=self.table_type))
    for c in ['index_axes', 'non_index_axes', 'values_axes']:
        sv = getattr(self, c, None)
        ov = getattr(other, c, None)
        if sv != ov:
            for i, sax in enumerate(sv):
                oax = ov[i]
                if sax != oax:
                    raise ValueError(
                        'invalid combinate of [{c}] on appending data [{sax}] vs current table [{oax}]'
                        .format(c=c, sax=sax, oax=oax))
            raise Exception(
                'invalid combinate of [{c}] on appending data [{sv}] vs current table [{ov}]'
                .format(c=c, sv=sv, ov=ov))