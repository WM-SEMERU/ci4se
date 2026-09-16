def get_fields(config):
    for data in config['scraping']['data']:
        if data['field'] != '':
            yield data['field']
    if 'next' in config['scraping']:
        for n in config['scraping']['next']:
            for f in get_fields(n):
                yield f