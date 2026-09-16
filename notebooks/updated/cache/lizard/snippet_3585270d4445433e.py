def get_sdb_path(self, sdb):
    sdb_id = self.get_sdb_id(sdb)
    sdb_resp = get_with_retry(self.cerberus_url + '/v1/safe-deposit-box/' +
        sdb_id + '/', headers=self.HEADERS)
    throw_if_bad_response(sdb_resp)
    return sdb_resp.json()['path']