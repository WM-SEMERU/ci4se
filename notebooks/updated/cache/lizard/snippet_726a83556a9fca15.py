def get_attributes(self, obj):
    return self._get_attributes('{}/{}'.format(self.session_url, obj.ref))