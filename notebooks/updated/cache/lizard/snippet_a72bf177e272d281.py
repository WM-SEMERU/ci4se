def watch(ctx):
    watcher = Watcher(ctx)
    watcher.watch_directory(path='{pkg.source_less}', ext='.less', action=
        lambda e: build(ctx, less=True))
    watcher.watch_directory(path='{pkg.source_js}', ext='.jsx', action=lambda
        e: build(ctx, js=True))
    watcher.watch_directory(path='{pkg.docs}', ext='.rst', action=lambda e:
        build(ctx, docs=True))
    watcher.start()