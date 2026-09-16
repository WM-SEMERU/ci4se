def save_and_validate_logo(logo_stream, logo_filename, community_id):
    cfg = current_app.config
    logos_bucket_id = cfg['COMMUNITIES_BUCKET_UUID']
    logo_max_size = cfg['COMMUNITIES_LOGO_MAX_SIZE']
    logos_bucket = Bucket.query.get(logos_bucket_id)
    ext = os.path.splitext(logo_filename)[1]
    ext = ext[1:] if ext.startswith('.') else ext
    logo_stream.seek(SEEK_SET, SEEK_END)
    logo_size = logo_stream.tell()
    if logo_size > logo_max_size:
        return None
    if ext in cfg['COMMUNITIES_LOGO_EXTENSIONS']:
        key = '{0}/logo.{1}'.format(community_id, ext)
        logo_stream.seek(0)
        ObjectVersion.create(logos_bucket, key, stream=logo_stream, size=
            logo_size)
        return ext
    else:
        return None