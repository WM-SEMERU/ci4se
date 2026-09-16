def get_remote_info(url_id):
    try:
        data = _send_request(url_id)
    except Exception as e:
        sys.stderr.write('Seeder GET error: ')
        sys.stderr.write(str(e.message))
        return None
    return _convert_to_wakat_format(data)