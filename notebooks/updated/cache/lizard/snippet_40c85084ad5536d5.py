def download_as_file(fn, data=None):
    if data is None:
        raise HTTPError(500, 'This service require POST `data` parameter.')
    response.set_header('Content-Type', 'application/octet-stream')
    response.set_header('Content-Disposition', 'attachment; filename="%s"' % fn
        )
    return StringIO(data)