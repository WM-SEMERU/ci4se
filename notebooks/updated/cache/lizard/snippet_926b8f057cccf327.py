def get_global_rate_limit(self):
    r = urllib.request.urlopen(
        'https://archive.org/metadata/iamine-rate-limiter')
    j = json.loads(r.read().decode('utf-8'))
    return int(j.get('metadata', {}).get('rate_per_second', 300))