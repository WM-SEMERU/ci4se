def create_temp_user_avatar(self, user, filename, size, avatar_img,
    contentType=None, auto_confirm=False):
    size_from_file = os.path.getsize(filename)
    if size != size_from_file:
        size = size_from_file
    filename = os.path.split(filename)[1]
    params = {'username': user, 'filename': filename, 'size': size}
    headers = {'X-Atlassian-Token': 'no-check'}
    if contentType is not None:
        headers['content-type'] = contentType
    else:
        headers['content-type'] = self._get_mime_type(avatar_img)
    url = self._get_url('user/avatar/temporary')
    r = self._session.post(url, params=params, headers=headers, data=avatar_img
        )
    cropping_properties = json_loads(r)
    if auto_confirm:
        return self.confirm_user_avatar(user, cropping_properties)
    else:
        return cropping_properties