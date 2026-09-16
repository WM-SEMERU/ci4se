def delete(self, tname, where=None, where_not=None, columns=None, astype=None):
    tname = self._check_tname(tname)
    where = PandasDatabase._check_conditions(where)
    where_not = PandasDatabase._check_conditions(where_not)
    columns = PandasDatabase._check_type_iter(str, columns)
    delrows = self.find(tname, where=where, where_not=where_not, astype=
        DataFrame)
    dataframe = self._db[tname]
    dataframe = dataframe[~dataframe.index.isin(delrows.index)]
    self._db[tname] = dataframe
    self._print('Deleted %d records from table "%s"' % (len(delrows), tname))
    if self.auto_save:
        self.save()
    return self._output(delrows, astype=astype)