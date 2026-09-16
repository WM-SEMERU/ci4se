def as_dict(self):
    d = {}
    for row in self:
        if row.time_slide_id not in d:
            d[row.time_slide_id] = offsetvector.offsetvector()
        if row.instrument in d[row.time_slide_id]:
            raise KeyError("'%s': duplicate instrument '%s'" % (row.
                time_slide_id, row.instrument))
        d[row.time_slide_id][row.instrument] = row.offset
    return d