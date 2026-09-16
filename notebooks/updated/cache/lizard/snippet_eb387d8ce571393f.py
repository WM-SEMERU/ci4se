def _ISO8601_to_UNIXtime(iso):
    try:
        d = datetime.strptime(iso, '%Y-%m-%d %H:%M:%S+00')
    except ValueError:
        raise ValueError(__name__ +
            ": bad format for input ISO8601 string, '             'should have been: YYYY-MM-DD HH:MM:SS+00"
            )
    return _datetime_to_UNIXtime(d)