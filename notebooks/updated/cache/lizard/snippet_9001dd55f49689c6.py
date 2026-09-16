def row(self, row_key, filter_=None, append=False):
    if append and filter_ is not None:
        raise ValueError('At most one of filter_ and append can be set')
    if append:
        return AppendRow(row_key, self)
    elif filter_ is not None:
        return ConditionalRow(row_key, self, filter_=filter_)
    else:
        return DirectRow(row_key, self)