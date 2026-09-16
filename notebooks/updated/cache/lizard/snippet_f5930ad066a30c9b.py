def remember_password(ctx, forget, clear_all):
    controller = ctx.obj['controller']
    settings = ctx.obj['settings']
    keys = settings.setdefault('keys', {})
    if clear_all:
        del settings['keys']
        settings.write()
        click.echo('All passwords have been cleared.')
    elif forget:
        if controller.id in keys:
            del keys[controller.id]
            settings.write()
        click.echo('Password forgotten.')
    else:
        ensure_validated(ctx, remember=True)