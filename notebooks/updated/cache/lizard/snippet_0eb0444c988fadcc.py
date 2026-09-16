def by_account(self, region, encrypted_account_id):
    url, query = SummonerApiV4Urls.by_account(region=region,
        encrypted_account_id=encrypted_account_id)
    return self._raw_request(self.by_account.__name__, region, url, query)