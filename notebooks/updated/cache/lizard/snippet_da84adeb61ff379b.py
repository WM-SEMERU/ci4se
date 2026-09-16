def save_catalog(filename, catalog, meta=None, prefix=None):
    ascii_table_formats = {'csv': 'csv', 'tab': 'tab', 'tex': 'latex',
        'html': 'html'}
    meta = update_meta_data(meta)
    extension = os.path.splitext(filename)[1][1:].lower()
    if extension in ['ann', 'reg']:
        writeAnn(filename, catalog, extension)
    elif extension in ['db', 'sqlite']:
        writeDB(filename, catalog, meta)
    elif extension in ['hdf5', 'fits', 'vo', 'vot', 'xml']:
        write_catalog(filename, catalog, extension, meta, prefix=prefix)
    elif extension in ascii_table_formats.keys():
        write_catalog(filename, catalog, fmt=ascii_table_formats[extension],
            meta=meta, prefix=prefix)
    else:
        log.warning('extension not recognised {0}'.format(extension))
        log.warning('You get tab format')
        write_catalog(filename, catalog, fmt='tab', prefix=prefix)
    return