def create_table_from_csv(self, csv_source, table_name='', attr_names=(),
    delimiter=',', quotechar='"', encoding='utf-8', primary_key=None,
    add_primary_key_column=False, index_attrs=None):
    import pytablereader as ptr
    loader = ptr.CsvTableFileLoader(csv_source)
    if typepy.is_not_null_string(table_name):
        loader.table_name = table_name
    loader.headers = attr_names
    loader.delimiter = delimiter
    loader.quotechar = quotechar
    loader.encoding = encoding
    try:
        for table_data in loader.load():
            self.__create_table_from_tabledata(table_data, primary_key,
                add_primary_key_column, index_attrs)
        return
    except (ptr.InvalidFilePathError, IOError):
        pass
    loader = ptr.CsvTableTextLoader(csv_source)
    if typepy.is_not_null_string(table_name):
        loader.table_name = table_name
    loader.headers = attr_names
    loader.delimiter = delimiter
    loader.quotechar = quotechar
    loader.encoding = encoding
    for table_data in loader.load():
        self.__create_table_from_tabledata(table_data, primary_key,
            add_primary_key_column, index_attrs)