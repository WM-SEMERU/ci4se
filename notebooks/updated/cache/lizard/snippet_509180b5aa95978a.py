def last_modified_time(path):
    return pd.Timestamp(os.path.getmtime(path), unit='s', tz='UTC')