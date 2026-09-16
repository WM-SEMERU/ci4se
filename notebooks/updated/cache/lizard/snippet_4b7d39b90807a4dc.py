def truncate(message, limit=500):
    if len(message) > limit:
        trc_msg = ''.join([message[:limit // 2 - 2], ' .. ', message[len(
            message) - limit // 2 + 2:]])
    else:
        trc_msg = message
    return trc_msg