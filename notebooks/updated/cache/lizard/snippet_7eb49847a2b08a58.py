def verify_permitted_to_read(gs_path):
    from . import _bucket
    bucket, prefix = _bucket.parse_name(gs_path)
    credentials = None
    if google.datalab.Context._is_signed_in():
        credentials = google.datalab.Context.default().credentials
    args = {'maxResults': Api._MAX_RESULTS, 'projection': 'noAcl'}
    if prefix is not None:
        args['prefix'] = prefix
    url = Api._ENDPOINT + Api._OBJECT_PATH % (bucket, '')
    try:
        google.datalab.utils.Http.request(url, args=args, credentials=
            credentials)
    except google.datalab.utils.RequestException as e:
        if e.status == 401:
            raise Exception(
                'Not permitted to read from specified path. Please sign in and make sure you have read access.'
                )
        raise e