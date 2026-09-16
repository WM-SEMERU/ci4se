def get_access_datetime(filepath):
    import tzlocal
    tz = tzlocal.get_localzone()
    mtime = datetime.fromtimestamp(os.path.getatime(filepath))
    return mtime.replace(tzinfo=tz)