def confirm_user_avatar(self, user, cropping_properties):
    data = cropping_properties
    url = self._get_url('user/avatar')
    r = self._session.post(url, params={'username': user}, data=json.dumps(
        data))
    return json_loads(r)