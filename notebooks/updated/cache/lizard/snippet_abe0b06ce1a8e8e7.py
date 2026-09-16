def PKCS_GET_query(self, req_hook, req_args):
    headers = {'content-type': 'application/json', 'sessionToken': self.
        __session__}
    try:
        if req_args is None:
            response = requests.get(self.__url__ + req_hook, headers=
                headers, cert=(self.__crt__, self.__key__), verify=True)
        else:
            response = requests.get(self.__url__ + req_hook + str(req_args),
                headers=headers, cert=(self.__crt__, self.__key__), verify=True
                )
    except requests.exceptions.RequestException as err:
        self.logger.error(err)
        return '500', 'Internal Error in PKCS_RESTful.GET_query()'
    self.logger.debug('%s: %s' % (response.status_code, response.text))
    return response.status_code, response.text