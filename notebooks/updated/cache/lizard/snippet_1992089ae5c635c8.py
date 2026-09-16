def create_response_dic(self):
    dic = {}
    for scope in self.scopes:
        if scope in self._scopes_registered():
            dic.update(getattr(self, 'scope_' + scope)())
    dic = self._clean_dic(dic)
    return dic