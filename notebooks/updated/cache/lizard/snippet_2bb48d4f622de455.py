def _get_result(self):
    info = {}
    self.options2attr = {'email': self._email, 'telephone': self._telephone,
        'QQ': self._QQ, 'wechat': self._wechat, 'url': self._url, 'emoji':
        self._emoji, 'tex': self._tex, 'blur': self._blur, 'message': self.m}
    for item in self.option:
        info[item] = self.options2attr[item]
    return info