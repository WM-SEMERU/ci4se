def make_url(self, method):
    token = self.settings()['token']
    return TELEGRAM_URL.format(token=quote(token), method=quote(method))