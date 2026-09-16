def configure_engine(cls, url: Union[str, URL, Dict[str, Any]]=None, bind:
    Union[Connection, Engine]=None, session: Dict[str, Any]=None,
    ready_callback: Union[Callable[[Engine, sessionmaker], Any], str]=None,
    poolclass: Union[str, Pool]=None, **engine_args):
    assert check_argument_types()
    if bind is None:
        if isinstance(url, dict):
            url = URL(**url)
        elif isinstance(url, str):
            url = make_url(url)
        elif url is None:
            raise TypeError('both "url" and "bind" cannot be None')
        if isinstance(poolclass, str):
            poolclass = resolve_reference(poolclass)
        if url.get_dialect().name == 'sqlite':
            connect_args = engine_args.setdefault('connect_args', {})
            connect_args.setdefault('check_same_thread', False)
        bind = create_engine(url, poolclass=poolclass, **engine_args)
    session = session or {}
    session.setdefault('expire_on_commit', False)
    ready_callback = resolve_reference(ready_callback)
    return bind, sessionmaker(bind, **session), ready_callback