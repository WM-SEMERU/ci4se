def download(self, path):
    service_get_resp = requests.get(self.location, cookies={'session': self
        .session})
    payload = service_get_resp.json()
    download_get_resp = requests.get(payload['content'])
    with open(path, 'wb') as config_file:
        config_file.write(download_get_resp.content)