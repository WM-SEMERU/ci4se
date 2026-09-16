def subroutine(*effects):

    def subroutine(value, context, *args, **kwargs):
        d = defer.succeed(value)
        for effect in effects:
            d.addCallback(effect, context, *args, **kwargs)
        return d
    return subroutine