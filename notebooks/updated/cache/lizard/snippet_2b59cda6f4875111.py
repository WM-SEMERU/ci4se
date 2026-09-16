def to_excel(self, path, na_rep='', engine=None, **kwargs):
    from pandas.io.excel import ExcelWriter
    if isinstance(path, str):
        writer = ExcelWriter(path, engine=engine)
    else:
        writer = path
    kwargs['na_rep'] = na_rep
    for item, df in self.iteritems():
        name = str(item)
        df.to_excel(writer, name, **kwargs)
    writer.save()