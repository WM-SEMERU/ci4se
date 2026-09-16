def create_rest_client_class(name, apis, BaseClass=RestClient):
    apis_with_actions = list(itertools.chain.from_iterable([zip([api] * len
        (api.actions), api.actions) for api in apis]))
    api_funcs = [create_api_call_func(api, verb) for api, verb in
        apis_with_actions]
    api_funcs.extend([create_async_api_call_func(api, verb) for api, verb in
        apis_with_actions])
    api_mapper = dict([(f.__name__, f) for f in api_funcs])

    def __init__(self, thread_count=_ASYNC_WORKER_THREAD_COUNT, **reqargs):
        BaseClass.__init__(self)
        setattr(self, 'reqargs', read_only_dict(reqargs))
        self._executor = concurrent.futures.ThreadPoolExecutor(thread_count)
    api_mapper['__init__'] = __init__
    ClientClass = type(_CLIENT_NAME_FMT.format(name), (BaseClass,), api_mapper)
    return ClientClass