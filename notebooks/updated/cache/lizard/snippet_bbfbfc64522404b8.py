def getDateReceived(self):
    request = self.getRequest()
    if request:
        ar_date = request.getDateReceived()
        if ar_date and self.created() > ar_date:
            return self.created()
        return ar_date
    return None