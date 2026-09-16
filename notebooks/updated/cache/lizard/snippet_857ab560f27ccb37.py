def pushover(message, token, user, title='JCVI: Job Monitor', priority=0,
    timestamp=None):
    assert -1 <= priority <= 2, 'Priority should be an int() between -1 and 2'
    if timestamp == None:
        from time import time
        timestamp = int(time())
    retry, expire = (300, 3600) if priority == 2 else (None, None)
    conn = HTTPSConnection('api.pushover.net:443')
    conn.request('POST', '/1/messages.json', urlencode({'token': token,
        'user': user, 'message': message, 'title': title, 'priority':
        priority, 'timestamp': timestamp, 'retry': retry, 'expire': expire}
        ), {'Content-type': 'application/x-www-form-urlencoded'})
    conn.getresponse()