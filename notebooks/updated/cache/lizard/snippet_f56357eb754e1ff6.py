def _mini_purge(self, spiderid, appid, crawlid):
    total_purged = 0
    match_string = '{sid}:*:queue'.format(sid=spiderid)
    for key in self.redis_conn.scan_iter(match=match_string):
        for item in self.redis_conn.zscan_iter(key):
            item_key = item[0]
            item = ujson.loads(item_key)
            if 'meta' in item:
                item = item['meta']
            if item['appid'] == appid and item['crawlid'] == crawlid:
                self.redis_conn.zrem(key, item_key)
                total_purged = total_purged + 1
    return total_purged