def fetch_bug_details(self, bug_ids):
    params = {'include_fields': 'product, component, priority, whiteboard, id'}
    params['id'] = bug_ids
    try:
        response = self.session.get(settings.BZ_API_URL + '/rest/bug',
            headers=self.session.headers, params=params, timeout=30)
        response.raise_for_status()
    except RequestException as e:
        logger.warning('error fetching bugzilla metadata for bugs due to {}'
            .format(e))
        return None
    if response.headers['Content-Type'] == 'text/html; charset=UTF-8':
        return None
    data = response.json()
    if 'bugs' not in data:
        return None
    return data['bugs']