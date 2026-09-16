def get_data_id_by_slug(self, slug):
    resolwe_host = os.environ.get('RESOLWE_HOST_URL')
    url = urllib.parse.urljoin(resolwe_host, '/api/data?slug={}&fields=id'.
        format(slug))
    with urllib.request.urlopen(url, timeout=60) as f:
        data = json.loads(f.read().decode('utf-8'))
    if len(data) == 1:
        return data[0]['id']
    elif not data:
        raise ValueError('Data not found for slug {}'.format(slug))
    else:
        raise ValueError('More than one data object returned for slug {}'.
            format(slug))