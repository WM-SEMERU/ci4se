def extract(self, m):
    self._clear()
    self.m = m
    if self.option != []:
        self._url_filter()
        self._email_filter()
        if 'tex' in self.option:
            self._tex_filter()
        if 'telephone' in self.option:
            self._telephone_filter()
        if 'QQ' in self.option:
            self._QQ_filter()
        if 'emoji' in self.option:
            self._emoji_filter()
        if 'wechat' in self.option:
            self._wechat_filter()
    self._filter()
    if 'blur' in self.option:
        self._blur = get_number(self.m, self._limit)
    return self._get_result()