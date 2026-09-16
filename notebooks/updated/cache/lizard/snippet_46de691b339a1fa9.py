def guestfs_conn_ro(disk):
    disk_path = os.path.expandvars(disk)
    conn = guestfs.GuestFS(python_return_dict=True)
    conn.add_drive_ro(disk_path)
    conn.set_backend(os.environ.get('LIBGUESTFS_BACKEND', 'direct'))
    try:
        conn.launch()
    except RuntimeError as err:
        LOGGER.debug(err)
        raise GuestFSError(
            'failed starting guestfs in readonly mode for disk: {0}'.format
            (disk))
    try:
        yield conn
    finally:
        conn.shutdown()
        conn.close()