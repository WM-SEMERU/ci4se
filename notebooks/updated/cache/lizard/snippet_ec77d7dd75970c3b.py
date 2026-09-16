def user_avatar_update(self, userid, payload):
    response, status_code = (self.__pod__.User.
        post_v1_admin_user_uid_avatar_update(sessionToken=self.__session,
        uid=userid, payload=payload).result())
    self.logger.debug('%s: %s' % (status_code, response))
    return status_code, response