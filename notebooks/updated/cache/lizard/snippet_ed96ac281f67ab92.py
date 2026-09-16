def search_results_info(self):
    if self._search_results_info is not None:
        return self._search_results_info
    try:
        info_path = self.input_header['infoPath']
    except KeyError:
        return None

    def convert_field(field):
        return (field[1:] if field[0] == '_' else field).replace('.', '_')

    def convert_value(field, value):
        if field == 'countMap':
            split = value.split(';')
            value = dict((key, int(value)) for key, value in zip(split[0::2
                ], split[1::2]))
        elif field == 'vix_families':
            value = ElementTree.fromstring(value)
        elif value == '':
            value = None
        else:
            try:
                value = float(value)
                if value.is_integer():
                    value = int(value)
            except ValueError:
                pass
        return value
    with open(info_path, 'rb') as f:
        from collections import namedtuple
        import csv
        reader = csv.reader(f, dialect='splunklib.searchcommands')
        fields = [convert_field(x) for x in reader.next()]
        values = [convert_value(f, v) for f, v in zip(fields, reader.next())]
    search_results_info_type = namedtuple('SearchResultsInfo', fields)
    self._search_results_info = search_results_info_type._make(values)
    return self._search_results_info