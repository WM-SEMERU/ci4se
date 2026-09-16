def piv(ctx):
    try:
        ctx.obj['controller'] = PivController(ctx.obj['dev'].driver)
    except APDUError as e:
        if e.sw == SW.NOT_FOUND:
            ctx.fail("The PIV application can't be found on this YubiKey.")
        raise