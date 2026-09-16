def list_(prefix='', region=None, key=None, keyid=None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)

    def extract_name(queue_url):
        return _urlparse(queue_url).path.split('/')[2]
    try:
        r = conn.list_queues(QueueNamePrefix=prefix)
        urls = r.get('QueueUrls', [])
        return {'result': [extract_name(url) for url in urls]}
    except botocore.exceptions.ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}