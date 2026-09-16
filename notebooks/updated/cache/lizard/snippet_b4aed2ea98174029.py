def create_session(self):
    ret = requests.Session()
    ret.headers['User-Agent'] = self.user_agent
    for k, v in self.options.items():
        setattr(ret, k, v)
    return ret