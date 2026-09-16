def users_info(self, user_id=None, username=None, **kwargs):
    if user_id:
        return self.__call_api_get('users.info', userId=user_id, kwargs=kwargs)
    elif username:
        return self.__call_api_get('users.info', username=username, kwargs=
            kwargs)
    else:
        raise RocketMissingParamException('userID or username required')