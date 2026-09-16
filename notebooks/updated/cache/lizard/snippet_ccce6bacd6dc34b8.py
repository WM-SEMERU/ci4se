def issue(self, CorpNum, MgtKey, Memo=None, UserID=None):
    if MgtKey == None or MgtKey == '':
        raise PopbillException(-99999999, '관리번호가 입력되지 않았습니다.')
    postData = ''
    req = {}
    if Memo != None or Memo != '':
        req['memo'] = Memo
    postData = self._stringtify(req)
    return self._httppost('/Cashbill/' + MgtKey, postData, CorpNum, UserID,
        'ISSUE')