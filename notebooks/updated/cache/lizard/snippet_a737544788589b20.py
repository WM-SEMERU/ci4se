def fetch_access_token(self):
    return self._fetch_access_token(url=
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken', params={'corpid':
        self.corp_id, 'corpsecret': self.secret})