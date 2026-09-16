def seq_2_DbData(seq, vec=None):
    if vec is None:
        if isinstance(seq, DbData):
            return seq
        vec = DbData()
    if not isinstance(vec, DbData):
        raise TypeError('vec must be a tango.DbData')
    for e in seq:
        vec.append(e)
    return vec