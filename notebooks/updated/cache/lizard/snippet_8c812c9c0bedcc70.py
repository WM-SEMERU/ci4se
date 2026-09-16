def avail_images(conn=None, call=None):
    if call == 'action':
        raise SaltCloudSystemExit(
            'The avail_images function must be called with -f or --function, or with the --list-images option'
            )
    if conn is None:
        conn = get_conn()
    return conn.list_images()