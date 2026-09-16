def get_repo(self, full_name_or_id, lazy=False):
    assert isinstance(full_name_or_id, (str, unicode, int, long)
        ), full_name_or_id
    url_base = '/repositories/' if isinstance(full_name_or_id, int
        ) or isinstance(full_name_or_id, long) else '/repos/'
    url = '%s%s' % (url_base, full_name_or_id)
    if lazy:
        return Repository.Repository(self.__requester, {}, {'url': url},
            completed=False)
    headers, data = self.__requester.requestJsonAndCheck('GET', '%s%s' % (
        url_base, full_name_or_id))
    return Repository.Repository(self.__requester, headers, data, completed
        =True)