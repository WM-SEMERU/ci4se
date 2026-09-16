def XML(uri, tc, ps, **keywords):
    source = urllib.urlopen(uri, **keywords)
    enc = source.info().getencoding()
    if enc in ['7bit', '8bit', 'binary']:
        data = source
    else:
        data = StringIO.StringIO()
        mimetools.decode(source, data, enc)
        data.seek(0)
    dom = ps.readerclass().fromStream(data)
    return _child_elements(dom)[0]