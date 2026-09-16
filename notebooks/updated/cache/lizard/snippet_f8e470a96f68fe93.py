def get_file(self, file_hash, save_file_at):
    params = {'hash': file_hash, 'apikey': self.api_key}
    try:
        response = requests.get(self.base + 'download/', params=params,
            proxies=self.proxies, stream=True)
    except requests.RequestException as e:
        return dict(error=e.message)
    if response.status_code == requests.codes.ok:
        self.save_downloaded_file(file_hash, save_file_at, response.content)
        return response.content
    elif response.status_code == 403:
        return dict(error=
            'You tried to perform calls to functions for which you require a Private API key.'
            , response_code=response.status_code)
    elif response.status_code == 404:
        return dict(error='File not found.', response_code=response.status_code
            )
    else:
        return dict(response_code=response.status_code)