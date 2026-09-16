def size(self):
    if 'length' in self.metainfo['info']:
        return self.metainfo['info']['length']
    elif 'files' in self.metainfo['info']:
        return sum(fileinfo['length'] for fileinfo in self.metainfo['info']
            ['files'])