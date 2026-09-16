def post(self, request, data=None):
    headers = {'Authorization': 'Bearer ' + self.token}
    logging.debug(json.dumps(data, indent=4))
    p = requests.post(self.url + request, headers=headers, data=json.dumps(
        data))
    return json.loads(p.text)