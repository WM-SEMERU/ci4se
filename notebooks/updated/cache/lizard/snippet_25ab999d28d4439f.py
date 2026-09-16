async def send(self):
    path = 'Items/{}'.format(self.id)
    resp = await self.connector.post(path, data=self.object_dict, remote=False)
    if resp.status == 400:
        await EmbyObject(self.object_dict, self.connector).update()
        resp = await self.connector.post(path, data=self.object_dict,
            remote=False)
    return resp