def select_as_dataframe(self, table_name, columns=None, where=None, extra=None
    ):
    import pandas
    if columns is None:
        columns = self.fetch_attr_names(table_name)
    result = self.select(select=AttrList(columns), table_name=table_name,
        where=where, extra=extra)
    if result is None:
        return pandas.DataFrame()
    return pandas.DataFrame(result.fetchall(), columns=columns)