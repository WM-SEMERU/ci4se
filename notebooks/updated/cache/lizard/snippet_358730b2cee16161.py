def check_status(self):
    try:
        r = requests.get(self.host + '/status', auth=self.auth, timeout=(
            10.0, 10.0))
        if not r.status_code == requests.codes.ok:
            print('Problem connecting to server at %s' % self.host)
            print('status code: %s' % r.status_code)
            return False
        else:
            print('Connected to server at %s' % self.host)
            return True
    except (requests.exceptions.ConnectionError, requests.exceptions.
        MissingSchema, requests.exceptions.InvalidSchema) as e:
        print('Problem connecting to server at %s' % self.host)
        print('error: %s' % e)
        return False