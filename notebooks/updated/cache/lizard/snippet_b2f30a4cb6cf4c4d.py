def _fetch(self, resource, params):
    url = urijoin(self.base_url, 'v3', resource)
    do_fetch = True
    while do_fetch:
        logger.debug('Puppet forge client calls resource: %s params: %s',
            resource, str(params))
        r = self.fetch(url, payload=params)
        yield r.text
        json_data = r.json()
        if 'pagination' in json_data:
            next_url = json_data['pagination']['next']
            if next_url:
                url = urijoin(self.base_url, next_url)
                params = {}
            else:
                do_fetch = False
        else:
            do_fetch = False