def build_filename(self, binary):
    try:
        folder = self.builds[self.build_index]
        timestamp = re.search('([\\d\\-]+)-\\D.*', folder).group(1)
    except Exception:
        timestamp = self.date.strftime('%Y-%m-%d')
    return '%(TIMESTAMP)s-%(BRANCH)s-%(NAME)s' % {'TIMESTAMP': timestamp,
        'BRANCH': self.branch, 'NAME': binary}