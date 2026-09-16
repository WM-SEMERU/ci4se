def read_data(filename, data_format=None):
    if not os.path.exists(filename):
        raise ValueError('Filename {} does not exist'.format(filename))
    if not isinstance(data_format, MimeType):
        data_format = get_data_format(filename)
    if data_format.is_tiff_format():
        return read_tiff_image(filename)
    if data_format is MimeType.JP2:
        return read_jp2_image(filename)
    if data_format.is_image_format():
        return read_image(filename)
    try:
        return {MimeType.TXT: read_text, MimeType.CSV: read_csv, MimeType.
            JSON: read_json, MimeType.XML: read_xml, MimeType.GML: read_xml,
            MimeType.SAFE: read_xml}[data_format](filename)
    except KeyError:
        raise ValueError('Reading data format .{} is not supported'.format(
            data_format.value))