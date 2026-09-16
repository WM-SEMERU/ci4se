def get_records_from_basket(self, bskid, group_basket=False, read_cache=True):
    if bskid not in self.cached_baskets or not read_cache:
        if self.user:
            if group_basket:
                group_basket = '&category=G'
            else:
                group_basket = ''
            results = requests.get(self.server_url +
                '/yourbaskets/display?of=xm&bskid=' + str(bskid) +
                group_basket, cookies=self.cookies, stream=True)
        else:
            results = requests.get(self.server_url +
                '/yourbaskets/display_public?of=xm&bskid=' + str(bskid),
                stream=True)
    else:
        return self.cached_baskets[bskid]
    parsed_records = self._parse_results(results.raw, self.cached_records)
    self.cached_baskets[bskid] = parsed_records
    return parsed_records