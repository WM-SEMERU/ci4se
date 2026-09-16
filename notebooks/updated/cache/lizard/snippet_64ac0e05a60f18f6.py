def _request(self, method, path, params=None):
    url = self._base_url + path
    try:
        if method == 'GET':
            response = requests.get(url, timeout=TIMEOUT)
        elif method == 'POST':
            response = requests.post(url, params, timeout=TIMEOUT)
        elif method == 'PUT':
            response = requests.put(url, params, timeout=TIMEOUT)
        elif method == 'DELETE':
            response = requests.delete(url, timeout=TIMEOUT)
        if response:
            return response.json()
        else:
            return {'status': 'error'}
    except requests.exceptions.HTTPError:
        return {'status': 'error'}
    except requests.exceptions.Timeout:
        return {'status': 'offline'}
    except requests.exceptions.RequestException:
        return {'status': 'offline'}