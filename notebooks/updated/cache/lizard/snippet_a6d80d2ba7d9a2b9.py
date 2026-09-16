def identity(ctx, variant_id):
    if not variant_id:
        LOG.warning('Please provide a variant id')
        ctx.abort()
    adapter = ctx.obj['adapter']
    version = ctx.obj['version']
    LOG.info('Search variants {0}'.format(adapter))
    result = adapter.get_clusters(variant_id)
    if result.count() == 0:
        LOG.info('No hits for variant %s', variant_id)
        return
    for res in result:
        click.echo(res)