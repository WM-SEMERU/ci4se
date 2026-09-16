def fido(ctx):
    dev = ctx.obj['dev']
    if dev.is_fips:
        try:
            ctx.obj['controller'] = FipsU2fController(dev.driver)
        except Exception as e:
            logger.debug('Failed to load FipsU2fController', exc_info=e)
            ctx.fail('Failed to load FIDO Application.')
    else:
        try:
            ctx.obj['controller'] = Fido2Controller(dev.driver)
        except Exception as e:
            logger.debug('Failed to load Fido2Controller', exc_info=e)
            ctx.fail('Failed to load FIDO 2 Application.')