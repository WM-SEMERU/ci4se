def post(self, path, data={}):
    response = requests.post(API_URL + path, data=json.dumps(data), headers
        =self._set_headers())
    return self._check_response(response, self.post, path, data)