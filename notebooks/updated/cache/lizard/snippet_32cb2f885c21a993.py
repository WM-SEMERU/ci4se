def search_for_count(self, **args):
    if 'timeout' not in args.keys():
        timeout = self.TIMEOUT
    elif args['timeout']:
        timeout = args['timeout']
    args['timeout'] = timeout / 15
    if 'count' not in args.keys():
        raise EmailException('Count param not defined!')
    else:
        count = int(args['count'])
        del args['count']
    results = None
    timer = timeout
    count = 0
    while count < timer:
        try:
            results = self.search(**args)
        except EmailException:
            if count == 0:
                return []
        if results and len(results) == count:
            return results
        else:
            time.sleep(15)
            count += 15
    if count >= timer:
        raise EmailException('Failed to match criteria %s in %s minutes' %
            (args, timeout / 60))