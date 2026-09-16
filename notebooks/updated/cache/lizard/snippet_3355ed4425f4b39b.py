def get_collector_path(base_url=None):
    if not base_url:
        return '/v0/event'
    event_url = urlparse(base_url)
    event_path = urljoin(event_url.path, 'v0/event')
    if not event_path.startswith('/'):
        event_path = '/%s' % event_path
    if event_url.query:
        event_path = '?'.join([event_path, event_url.query])
    return event_path