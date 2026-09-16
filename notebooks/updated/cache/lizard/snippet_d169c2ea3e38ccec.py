def mementoweb_api_tags(url):
    memento_url = 'http://labs.mementoweb.org/timemap/json/'
    r = requests.get(memento_url + url)
    if r.status_code != 200:
        return []
    data = r.json().get('mementos', {}).get('list', [])
    if not data:
        return []
    resources = (TimeResource(url=item.get('uri', ''), date=item.get(
        'datetime', ''), val=item.get('datetime', '').split('-')[0], source
        ='MementoWeb.org') for item in data)
    resource_dict = {res.val: res for res in resources}
    return sorted(resource_dict.values(), key=lambda x: x.val)