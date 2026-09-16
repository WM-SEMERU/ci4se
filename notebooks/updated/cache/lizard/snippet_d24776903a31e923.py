def get_authserver(self, domainid, serverid):
    return self.api_call(ENDPOINTS['authservers']['get'], dict(domainid=
        domainid, serverid=serverid))