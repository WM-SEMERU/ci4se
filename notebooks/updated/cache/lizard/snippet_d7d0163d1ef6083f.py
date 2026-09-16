def getLipdNames(D=None):
    _names = []
    try:
        if not D:
            print(
                'Error: LiPD data not provided. Pass LiPD data into the function.'
                )
        else:
            _names = D.keys()
    except Exception:
        pass
    return _names