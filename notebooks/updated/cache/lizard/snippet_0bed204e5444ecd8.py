def pyeapi_call(method, *args, **kwargs):
    pyeapi_kwargs = pyeapi_nxos_api_args(**kwargs)
    return __salt__['pyeapi.call'](method, *args, **pyeapi_kwargs)