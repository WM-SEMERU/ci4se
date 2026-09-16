def _adjustSyllabification(adjustedPhoneList, syllableList):
    i = 0
    retSyllableList = []
    for syllableNum, syllable in enumerate(syllableList):
        j = len(syllable)
        if syllableNum == len(syllableList) - 1:
            j = len(adjustedPhoneList) - i
        tmpPhoneList = adjustedPhoneList[i:i + j]
        numBlanks = -1
        phoneList = tmpPhoneList[:]
        while numBlanks != 0:
            numBlanks = tmpPhoneList.count("''")
            if numBlanks > 0:
                tmpPhoneList = adjustedPhoneList[i + j:i + j + numBlanks]
                phoneList.extend(tmpPhoneList)
                j += numBlanks
        for k, phone in enumerate(phoneList):
            if phone == "''":
                syllable.insert(k, "''")
        i += j
        retSyllableList.append(syllable)
    return retSyllableList