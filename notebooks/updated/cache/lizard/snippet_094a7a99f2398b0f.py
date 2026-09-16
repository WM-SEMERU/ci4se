def get_user_info(self, token):
    url = self.get_user_info_url()
    try:
        headers = {'Authorization': 'Bearer {}'.format(token)}
        response = requests.get(url, headers=headers)
    except requests.RequestException:
        logger.exception(
            'Failed to retrieve user info due to a request exception.')
        raise UserInfoRetrievalFailed
    if response.status_code == 200:
        return self.process_user_info_response(response.json())
    else:
        msg = (
            'Failed to retrieve user info. Server [{server}] responded with status [{status}].'
            .format(server=url, status=response.status_code))
        raise UserInfoRetrievalFailed(msg)