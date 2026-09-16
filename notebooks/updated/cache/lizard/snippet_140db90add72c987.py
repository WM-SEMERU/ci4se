def match_mopfiles(mopfile1, mopfile2):
    pos1 = pos2 = numpy.array([])
    if len(mopfile1.data) > 0:
        X_COL = 'X_{}'.format(mopfile1.header.file_ids[0])
        Y_COL = 'Y_{}'.format(mopfile1.header.file_ids[0])
        pos1 = numpy.array([mopfile1.data[X_COL].data, mopfile1.data[Y_COL]
            .data]).transpose()
    if len(mopfile2.data) > 0:
        X_COL = 'X_{}'.format(mopfile2.header.file_ids[0])
        Y_COL = 'Y_{}'.format(mopfile2.header.file_ids[0])
        pos2 = numpy.array([mopfile2.data[X_COL].data, mopfile2.data[Y_COL]
            .data]).transpose()
    match_idx1, match_idx2 = util.match_lists(pos1, pos2)
    mopfile1.data.add_column(Column(data=match_idx1.filled(-1), name='real',
        length=len(mopfile1.data)))
    idx = 0
    for file_id in mopfile1.header.file_ids:
        idx += 1
        mopfile1.data.add_column(Column(data=[file_id] * len(mopfile1.data),
            name='ID_{}'.format(idx)))
    return mopfile1