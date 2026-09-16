def __is_current(filepath):
    if not __DOWNLOAD_PARAMS['auto_update']:
        return True
    if not os.path.isfile(filepath):
        return False
    return datetime.datetime.utcfromtimestamp(os.path.getmtime(filepath)
        ) > __get_last_update_time()