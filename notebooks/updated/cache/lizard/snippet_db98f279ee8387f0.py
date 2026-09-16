def map_providers_parallel(self, query='list_nodes', cached=False):
    if cached is True and query in self.__cached_provider_queries:
        return self.__cached_provider_queries[query]
    opts = self.opts.copy()
    multiprocessing_data = []
    opts['providers'] = self._optimize_providers(opts['providers'])
    for alias, drivers in six.iteritems(opts['providers']):
        this_query = query
        for driver, details in six.iteritems(drivers):
            if opts.get('selected_query_option'
                ) is None and '{0}.list_nodes_min'.format(driver
                ) in self.clouds:
                this_query = 'list_nodes_min'
            fun = '{0}.{1}'.format(driver, this_query)
            if fun not in self.clouds:
                log.error('Public cloud provider %s is not available', driver)
                continue
            multiprocessing_data.append({'fun': fun, 'opts': opts, 'query':
                this_query, 'alias': alias, 'driver': driver})
    output = {}
    if not multiprocessing_data:
        return output
    data_count = len(multiprocessing_data)
    pool = multiprocessing.Pool(data_count < 10 and data_count or 10,
        init_pool_worker)
    parallel_pmap = enter_mainloop(_run_parallel_map_providers_query,
        multiprocessing_data, pool=pool)
    for alias, driver, details in parallel_pmap:
        if not details:
            continue
        if alias not in output:
            output[alias] = {}
        output[alias][driver] = details
    self.__cached_provider_queries[query] = output
    return output