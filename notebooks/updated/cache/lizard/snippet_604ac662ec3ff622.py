def sendEmail(self, emails, massType='SingleEmailMessage'):
    return SendEmailRequest(self.__serverUrl, self.sessionId, emails, massType
        ).post(self.__conn)