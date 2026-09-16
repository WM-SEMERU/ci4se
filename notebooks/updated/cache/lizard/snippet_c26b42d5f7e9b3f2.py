def get_export(request):
    settings = get_current_registry().settings
    exports_dirs = settings['exports-directories'].split()
    args = request.matchdict
    ident_hash, type = args['ident_hash'], args['type']
    id, version = split_ident_hash(ident_hash)
    with db_connect() as db_connection:
        with db_connection.cursor() as cursor:
            try:
                results = get_export_files(cursor, id, version, [type],
                    exports_dirs, read_file=True)
                if not results:
                    raise httpexceptions.HTTPNotFound()
                filename, mimetype, size, modtime, state, file_content = (
                    results[0])
            except ExportError as e:
                logger.debug(str(e))
                raise httpexceptions.HTTPNotFound()
    if state == 'missing':
        raise httpexceptions.HTTPNotFound()
    encoded_filename = urllib.quote(filename.encode('utf-8'))
    resp = request.response
    resp.status = '200 OK'
    resp.content_type = mimetype
    resp.content_disposition = (
        "attachment; filename={fname}; filename*=UTF-8''{fname}".format(
        fname=encoded_filename))
    resp.body = file_content
    slug_title = '-'.join(encoded_filename.split('-')[:-1])
    resp.headerlist.append(('Link',
        '<https://{}/contents/{}/{}> ;rel="Canonical"'.format(request.host,
        id, slug_title)))
    return resp