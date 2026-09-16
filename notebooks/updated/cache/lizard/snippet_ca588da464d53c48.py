def createGroup(self, title, tags, description='', snippet='', phone='',
    access='org', sortField='title', sortOrder='asc', isViewOnly=False,
    isInvitationOnly=False, thumbnail=None):
    params = {'f': 'json', 'title': title, 'description': description,
        'snippet': snippet, 'tags': tags, 'phone': phone, 'access': access,
        'sortField': sortField, 'sortOrder': sortOrder, 'isViewOnly':
        isViewOnly, 'isInvitationOnly': isInvitationOnly}
    url = self._url + '/createGroup'
    groups = self.groups
    if thumbnail is not None and os.path.isfile(thumbnail):
        res = self._post(url=url, param_dict=params, files={'thumbnail':
            thumbnail}, securityHandler=self._securityHandler, proxy_url=
            self._proxy_url, proxy_port=self._proxy_port)
    else:
        res = self._post(url=url, param_dict=params, securityHandler=self.
            _securityHandler, proxy_url=self._proxy_url, proxy_port=self.
            _proxy_port)
    if 'group' not in res:
        raise Exception('%s' % res)
    if 'id' not in res['group']:
        raise Exception('%s' % res)
    groupId = res['group']['id']
    url = '%s/groups/%s' % (self.root, groupId)
    return Group(url=url, securityHandler=self._securityHandler, proxy_url=
        self._proxy_url, proxy_port=self._proxy_port, initalize=False)