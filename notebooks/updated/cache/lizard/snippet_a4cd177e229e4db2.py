def createSite(self, username, password, fullname, email, description,
    securityQuestionIdx, secuirtyQuestionAns, contentDir):
    params = {'username': username, 'password': password, 'fullname':
        fullname, 'email': email, 'description': description,
        'secuirtyQuestionAns': secuirtyQuestionAns, 'securityQuestionIdx':
        securityQuestionIdx, 'contentDir': contentDir}
    url = self._url + '/createNewSite'
    return self._get(url=url, param_dict=params)