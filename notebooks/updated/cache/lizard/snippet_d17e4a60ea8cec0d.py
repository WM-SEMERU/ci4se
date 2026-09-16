def export_users(self, format='json'):
    pl = self.__basepl(content='user', format=format)
    return self._call_api(pl, 'exp_user')[0]