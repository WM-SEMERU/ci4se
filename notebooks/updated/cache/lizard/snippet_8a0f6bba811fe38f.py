def demo(ctx, reset=False):
    if reset:
        rmdb(ctx)
    ctx.run('demo check', pty=True)
    ctx.run('demo loaddemo', pty=True)
    ctx.run('demo runserver', pty=True)