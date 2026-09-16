def read_sas(filepath_or_buffer, format=None, index=None, encoding=None,
    chunksize=None, iterator=False):
    if format is None:
        buffer_error_msg = (
            'If this is a buffer object rather than a string name, you must specify a format string'
            )
        filepath_or_buffer = _stringify_path(filepath_or_buffer)
        if not isinstance(filepath_or_buffer, str):
            raise ValueError(buffer_error_msg)
        fname = filepath_or_buffer.lower()
        if fname.endswith('.xpt'):
            format = 'xport'
        elif fname.endswith('.sas7bdat'):
            format = 'sas7bdat'
        else:
            raise ValueError('unable to infer format of SAS file')
    if format.lower() == 'xport':
        from pandas.io.sas.sas_xport import XportReader
        reader = XportReader(filepath_or_buffer, index=index, encoding=
            encoding, chunksize=chunksize)
    elif format.lower() == 'sas7bdat':
        from pandas.io.sas.sas7bdat import SAS7BDATReader
        reader = SAS7BDATReader(filepath_or_buffer, index=index, encoding=
            encoding, chunksize=chunksize)
    else:
        raise ValueError('unknown SAS format')
    if iterator or chunksize:
        return reader
    data = reader.read()
    reader.close()
    return data