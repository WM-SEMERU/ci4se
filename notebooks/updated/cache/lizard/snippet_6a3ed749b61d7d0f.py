def _calculate_session_expiry(self, request, user_info):
    access_token_expiry_timestamp = self._get_access_token_expiry(request)
    id_token_expiry_timestamp = self._get_id_token_expiry(user_info)
    now_in_seconds = int(time.time())
    earliest_expiration_timestamp = min(access_token_expiry_timestamp,
        id_token_expiry_timestamp)
    seconds_until_expiry = earliest_expiration_timestamp - now_in_seconds
    if seconds_until_expiry <= 0:
        raise AuthError('Session expiry time has already passed!')
    return seconds_until_expiry