def sign_report(self, device_id, root, data, **kwargs):
    report_key = self._verify_derive_key(device_id, root, **kwargs)
    message_hash = hashlib.sha256(data).digest()
    hmac_calc = hmac.new(report_key, message_hash, hashlib.sha256)
    result = bytearray(hmac_calc.digest())
    return {'signature': result, 'root_key': root}