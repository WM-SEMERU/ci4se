def update(self, file):
    params = {'message': file.logs, 'author': file.author.dict(), 'content':
        file.base64, 'sha': file.blob, 'branch': file.branch}
    uri = '{api}/repos/{origin}/contents/{path}'.format(api=self.
        github_api_url, origin=self.origin, path=file.path)
    data = self.request('PUT', uri, data=params)
    if data.status_code == 200:
        file.pushed = True
        return file
    else:
        reply = json.loads(data.content.decode('utf-8'))
        return self.ProxyError(data.status_code, (reply, 'message'), step=
            'update', context={'uri': uri, 'params': params})