def _paged_api_call(self, func, kwargs, item_type='photo'):
    page = 1
    while True:
        LOG.info('Fetching page %s' % page)
        kwargs['page'] = page
        rsp = self._load_rsp(func(**kwargs))
        if rsp['stat'] == 'ok':
            plural = item_type + 's'
            if plural in rsp:
                items = rsp[plural]
                if int(items['page']) < page:
                    LOG.info(
                        'End of Flickr pages (%s pages with %s per page)' %
                        (items['pages'], items['perpage']))
                    break
                for i in items[item_type]:
                    yield self._prep(i)
            else:
                yield rsp
            page += 1
        else:
            yield [rsp]
            break