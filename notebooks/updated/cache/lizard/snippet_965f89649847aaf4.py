def users_get_presence(self, user_id=None, username=None, **kwargs):
    if user_id:
        return self.__call_api_get('users.getPresence', userId=user_id,
            kwargs=kwargs)
    elif username:
        return self.__call_api_get('users.getPresence', username=username,
            kwargs=kwargs)
    else:
        raise RocketMissingParamException('userID or username required')