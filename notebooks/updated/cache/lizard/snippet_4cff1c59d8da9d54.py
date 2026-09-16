def getUserInfo(self):
    userJson = self.httpGet(ReaderUrl.USER_INFO_URL)
    result = json.loads(userJson, strict=False)
    self.userId = result['userId']
    return result