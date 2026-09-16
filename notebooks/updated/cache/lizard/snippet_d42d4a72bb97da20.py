def register_product_key(self, key):
    resp = self.send_job_and_wait(MsgProto(EMsg.ClientRegisterKey), {'key':
        key}, timeout=30)
    if resp:
        details = vdf.binary_loads(resp.purchase_receipt_info).get(
            'MessageObject', None)
        return EResult(resp.eresult), resp.purchase_result_details, details
    else:
        return EResult.Timeout, None, None