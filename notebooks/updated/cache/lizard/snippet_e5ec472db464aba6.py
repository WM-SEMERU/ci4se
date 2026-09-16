def put(self, path_or_tuple, folder_id='0', file_id=None, file_etag=None):
    name, src = (basename(path_or_tuple), open(path_or_tuple)) if isinstance(
        path_or_tuple, types.StringTypes) else (path_or_tuple[0],
        path_or_tuple[1])
    folder_id = dict(parent_id=folder_id) if file_id is None else dict()
    return self(join('files', 'content') if file_id is None else join(
        'files', bytes(file_id), 'content'), method='post', upload=True,
        headers={'If-Match': file_etag} if file_etag else dict(), files=
        dict(filename=(name, src), **folder_id))