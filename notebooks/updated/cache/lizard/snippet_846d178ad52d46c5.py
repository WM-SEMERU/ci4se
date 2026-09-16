def teetsv(table, source=None, encoding=None, errors='strict', write_header
    =True, **csvargs):
    csvargs.setdefault('dialect', 'excel-tab')
    return teecsv(table, source=source, encoding=encoding, errors=errors,
        write_header=write_header, **csvargs)