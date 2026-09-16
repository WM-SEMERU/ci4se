def detect_tag(filename):
    with fileutil.opened(filename, 'rb') as file:
        file.seek(0)
        header = file.read(10)
        file.seek(0)
        if len(header) < 10:
            raise NoTagError('File too short')
        if header[0:3] != b'ID3':
            raise NoTagError('ID3v2 tag not found')
        if header[3] not in _tag_versions or header[4] != 0:
            raise TagError('Unknown ID3 version: 2.{0}.{1}'.format(*header[
                3:5]))
        cls = _tag_versions[header[3]]
        offset = 0
        length = Syncsafe.decode(header[6:10]) + 10
        if header[3] == 4 and header[5] & _TAG24_FOOTER:
            length += 10
        return cls, offset, length