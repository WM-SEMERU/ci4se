def by_summoner(self, region, encrypted_summoner_id):
    url, query = ThirdPartyCodeApiV4Urls.by_summoner(region=region,
        encrypted_summoner_id=encrypted_summoner_id)
    return self._raw_request(self.by_summoner.__name__, region, url, query)