def once(ctx, name):
    from kibitzr.app import Application
    app = Application()
    sys.exit(app.run(once=True, log_level=ctx.obj['log_level'], names=name))