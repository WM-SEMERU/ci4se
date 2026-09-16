def quality_to_apply(self):
    if self.request.quality is None:
        if self.api_version <= '1.1':
            return 'native'
        else:
            return 'default'
    return self.request.quality