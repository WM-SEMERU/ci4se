def delete_sdb(self, sdb_id):
    sdb_resp = delete_with_retry(self.cerberus_url +
        '/v2/safe-deposit-box/' + sdb_id, headers=self.HEADERS)
    throw_if_bad_response(sdb_resp)
    return sdb_resp