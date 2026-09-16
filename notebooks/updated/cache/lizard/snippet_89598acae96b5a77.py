def OpenUrlWithBasicAuth(url, user='root', pwd=''):
    return requests.get(url, auth=HTTPBasicAuth(user, pwd), verify=False)