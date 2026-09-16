def getMessageCharge(self, apiMsgId):
    content = self.parseLegacy(self.request('http/getmsgcharge', {
        'apimsgid': apiMsgId}))
    return {'id': apiMsgId, 'status': content['status'], 'description':
        self.getStatus(content['status']), 'charge': float(content['charge'])}