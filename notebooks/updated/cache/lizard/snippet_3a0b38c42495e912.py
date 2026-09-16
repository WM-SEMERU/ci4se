def _generate_processed_key_name(process_to, upload_name):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    name, extension = os.path.splitext(upload_name)
    digest = md5(''.join([timestamp, upload_name])).hexdigest()
    return os.path.join(process_to, '{0}.{1}'.format(digest, extension))