def get_infos_with_id(self, uid):
    _logid = uid
    _user_info_url = USER_INFO_URL.format(logid=_logid)
    return self._request_api(url=_user_info_url).json()