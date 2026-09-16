def getcloud(site, feed_id=None):
    cloudict = fjcache.cache_get(site.id, 'tagclouds')
    if not cloudict:
        cloudict = cloudata(site)
        fjcache.cache_set(site, 'tagclouds', cloudict)
    if feed_id:
        feed_id = int(feed_id)
        if feed_id in cloudict:
            return cloudict[feed_id]
        return []
    return cloudict[0]