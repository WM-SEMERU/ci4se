def search(self, q, max_id=None, since_id=None, lang=None, result_type=
    'recent', geocode=None, max_pages=None):
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    params = {'count': 100, 'q': q, 'include_ext_alt_text': 'true'}
    if lang is not None:
        params['lang'] = lang
    if result_type in ['mixed', 'recent', 'popular']:
        params['result_type'] = result_type
    else:
        params['result_type'] = 'recent'
    if geocode is not None:
        params['geocode'] = geocode
    retrieved_pages = 0
    reached_end = False
    while True:
        if since_id:
            params['since_id'] = str(int(since_id) - 1)
        if max_id:
            params['max_id'] = max_id
        resp = self.get(url, params=params)
        retrieved_pages += 1
        statuses = resp.json()['statuses']
        if len(statuses) == 0:
            log.info('no new tweets matching %s', params)
            break
        for status in statuses:
            if since_id is not None and status['id_str'] == str(since_id):
                reached_end = True
                break
            yield status
        if reached_end:
            log.info('no new tweets matching %s', params)
            break
        if max_pages is not None and retrieved_pages == max_pages:
            log.info('reached max page limit for %s', params)
            break
        max_id = str(int(status['id_str']) - 1)