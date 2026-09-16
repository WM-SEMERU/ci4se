async def update(self, fields=''):
    path = 'Users/{{UserId}}/Items/{}'.format(self.id)
    info = await self.connector.getJson(path, remote=False, Fields=
        'Path,Overview,' + fields)
    self.object_dict.update(info)
    self.extras = {}
    return self