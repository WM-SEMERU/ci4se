def embed(globals=None, locals=None, configure=None, vi_mode=False,
    history_filename=None, title=None, startup_paths=None, patch_stdout=
    False, return_asyncio_coroutine=False):
    assert configure is None or callable(configure)
    if globals is None:
        globals = {'__name__': '__main__', '__package__': None, '__doc__':
            None, '__builtins__': six.moves.builtins}
    locals = locals or globals

    def get_globals():
        return globals

    def get_locals():
        return locals
    if return_asyncio_coroutine:
        use_asyncio_event_loop()
    repl = PythonRepl(get_globals=get_globals, get_locals=get_locals,
        vi_mode=vi_mode, history_filename=history_filename, startup_paths=
        startup_paths)
    if title:
        repl.terminal_title = title
    if configure:
        configure(repl)
    app = repl.app
    patch_context = patch_stdout_context() if patch_stdout else DummyContext()
    if return_asyncio_coroutine:

        def coroutine():
            with patch_context:
                while True:
                    iterator = iter(app.run_async().to_asyncio_future())
                    try:
                        while True:
                            yield next(iterator)
                    except StopIteration as exc:
                        text = exc.args[0]
                    repl._process_text(text)
        return coroutine()
    else:
        with patch_context:
            repl.run()