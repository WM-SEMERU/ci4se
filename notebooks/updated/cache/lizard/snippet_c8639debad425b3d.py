def checkIsMember(self, CorpNum):
    if CorpNum == None or CorpNum == '':
        raise PopbillException(-99999999, '사업자번호가 입력되지 않았습니다.')
    return self._httpget('/Join?CorpNum=' + CorpNum + '&LID=' + self.
        __linkID, None, None)