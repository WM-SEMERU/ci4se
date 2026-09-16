def _release_info():
    pypi_url = 'http://pypi.python.org/pypi/fastfood/json'
    headers = {'Accept': 'application/json'}
    request = urllib.Request(pypi_url, headers=headers)
    response = urllib.urlopen(request).read().decode('utf_8')
    data = json.loads(response)
    return data