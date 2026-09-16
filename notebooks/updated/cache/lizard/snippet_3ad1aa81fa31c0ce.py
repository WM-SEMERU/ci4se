def fileupdate(self, data):
    self.name = data['name']
    add = self.__additional
    add['filetype'] = 'other'
    for filetype in ('book', 'image', 'video', 'audio', 'archive'):
        if filetype in data:
            add['filetype'] = filetype
            break
    if add['filetype'] in ('image', 'video', 'audio'):
        add['thumb'] = data.get('thumb', dict())
    add['checksum'] = data['checksum']
    add['expire_time'] = data['expires'] / 1000
    add['size'] = data['size']
    add['info'] = data.get(add['filetype'], dict())
    add['uploader'] = data['user']
    if self.room.admin:
        add['info'].update({'room': data.get('room')})
        add['info'].update({'uploader_ip': data.get('uploader_ip')})
    self.updated = True