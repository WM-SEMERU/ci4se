def cli(ctx, report, semantic, rcfile):
    ctx.obj = {'report': report, 'semantic': semantic, 'rcfile': rcfile}