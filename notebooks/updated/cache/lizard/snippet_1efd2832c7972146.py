def nack(self, id, subscription, transaction=None, receipt=None):
    assert id is not None, "'id' is required"
    assert subscription is not None, "'subscription' is required"
    headers = {HDR_MESSAGE_ID: id, HDR_SUBSCRIPTION: subscription}
    if transaction:
        headers[HDR_TRANSACTION] = transaction
    if receipt:
        headers[HDR_RECEIPT] = receipt
    self.send_frame(CMD_NACK, headers)