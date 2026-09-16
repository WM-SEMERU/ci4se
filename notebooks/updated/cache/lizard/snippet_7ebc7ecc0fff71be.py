def put(self, url, data=None, body=None):
    response = self.http.put(url, headers=self.headers, data=body, params=
        data, **self.requests_params)
    return self.process(response)