def CreateGallery():
    url = 'http://min.us/api/CreateGallery'
    response = _dopost(url)
    _editor_id = response['editor_id']
    _reader_id = response['reader_id']
    return Gallery(_reader_id, editor_id=_editor_id)