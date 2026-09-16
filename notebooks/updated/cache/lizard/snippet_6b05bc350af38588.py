def invoked(self, ctx):
    print('{} + {} = {}'.format(ctx.args.x, ctx.args.y, ctx.args.x + ctx.
        args.y))