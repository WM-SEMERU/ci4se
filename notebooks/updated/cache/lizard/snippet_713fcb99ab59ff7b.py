def checkMgtKeyInUse(self, CorpNum, MgtKeyType, MgtKey):
    if MgtKeyType not in self.__MgtKeyTypes:
        raise PopbillException(-99999999, '관리번호 형태가 올바르지 않습니다.')
    if MgtKey == None or MgtKey == '':
        raise PopbillException(-99999999, '관리번호가 입력되지 않았습니다.')
    try:
        result = self._httpget('/Taxinvoice/' + MgtKeyType + '/' + MgtKey,
            CorpNum)
        return result.itemKey != None and result.itemKey != ''
    except PopbillException as PE:
        if PE.code == -11000005:
            return False
        raise PE