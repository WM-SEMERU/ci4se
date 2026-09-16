def parse_changes(json):
    changes = []
    dates = len(json)
    for date in range(1, dates):
        last_close = json[date - 1]['close']
        now_close = json[date]['close']
        changes.append(now_close - last_close)
    logger.debug('Market Changes (from JSON):\n{0}'.format(changes))
    return changes