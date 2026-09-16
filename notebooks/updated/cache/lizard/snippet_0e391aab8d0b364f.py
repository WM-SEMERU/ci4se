def build_url(self, path):
    url = '{0}{1}'.format(self.base_url, path)
    url = re.sub('([^:])//', '\\1/', url)
    return url