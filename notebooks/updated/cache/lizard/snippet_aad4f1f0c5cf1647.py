def cancelSend(self, CorpNum, MgtKeyType, MgtKey, Memo=None, UserID=None):
    if MgtKeyType not in self.__MgtKeyTypes:
        raise PopbillException(-99999999, '관리번호 형태가 올바르지 않습니다.')
    if MgtKey == None or MgtKey == '':
        raise PopbillException(-99999999, '관리번호가 입력되지 않았습니다.')
    if Memo != None and Memo != '':
        postData = self._stringtify({'memo': Memo})
    else:
        postData = ''
    return self._httppost('/Taxinvoice/' + MgtKeyType + '/' + MgtKey,
        postData, CorpNum, UserID, 'CANCELSEND')