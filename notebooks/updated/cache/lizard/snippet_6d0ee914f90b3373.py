def ngfileupload_uploadfactory(content_length=None, content_type=None,
    uploaded_file=None):
    if not content_type.startswith('multipart/form-data'):
        abort(422)
    return uploaded_file.stream, content_length, None, parse_header_tags()