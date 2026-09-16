def restore_droplet(self, droplet_id, image_id):
    if not droplet_id:
        raise DOPException('droplet_id is required to restore a droplet!')
    if not image_id:
        raise DOPException('image_id is required to rebuild a droplet!')
    params = {'image_id': image_id}
    json = self.request('/droplets/%s/restore' % droplet_id, method='GET',
        params=params)
    status = json.get('status')
    if status == 'OK':
        return json.get('event_id')
    else:
        message = json.get('message')
        raise DOPException('[%s]: %s' % (status, message))