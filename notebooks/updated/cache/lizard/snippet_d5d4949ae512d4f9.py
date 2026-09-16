def get_user_id_by_user(self, username):
    response, status_code = self.__pod__.Users.get_v2_user(sessionToken=
        self.__session__, username=username).result()
    self.logger.debug('%s: %s' % (status_code, response))
    return status_code, response