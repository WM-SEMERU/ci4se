def extract(d, whichtables, mode, time):
    logger_ts.info('enter extract_main')
    _root = {}
    _ts = {}
    _pc = 'paleoData'
    if mode == 'chron':
        _pc = 'chronData'
    _root['mode'] = _pc
    _root['time_id'] = time
    try:
        for k, v in d.items():
            if k == 'funding':
                _root = _extract_fund(v, _root)
            elif k == 'geo':
                _root = _extract_geo(v, _root)
            elif k == 'pub':
                _root = _extract_pub(v, _root)
            elif k not in ['chronData', 'paleoData']:
                _root[k] = v
        _ts = _extract_pc(d, _root, _pc, whichtables)
    except Exception as e:
        logger_ts.error('extract: Exception: {}'.format(e))
        print('extract: Exception: {}'.format(e))
    logger_ts.info('exit extract_main')
    return _ts