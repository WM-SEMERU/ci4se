def get_file_hash(storage, path):
    contents = storage.open(path).read()
    file_hash = hashlib.md5(contents).hexdigest()
    content_type = mimetypes.guess_type(path)[0] or 'application/octet-stream'
    if settings.is_gzipped and content_type in settings.gzip_content_types:
        cache_key = get_cache_key('gzip_hash_%s' % file_hash)
        file_hash = cache.get(cache_key, False)
        if file_hash is False:
            buffer = BytesIO()
            zf = gzip.GzipFile(mode='wb', compresslevel=6, fileobj=buffer,
                mtime=0.0)
            zf.write(force_bytes(contents))
            zf.close()
            file_hash = hashlib.md5(buffer.getvalue()).hexdigest()
            cache.set(cache_key, file_hash)
    return '"%s"' % file_hash