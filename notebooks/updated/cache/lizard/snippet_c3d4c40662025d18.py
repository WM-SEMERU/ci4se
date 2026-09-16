def init(paths, output, **kwargs):
    dp = goodtables.init_datapackage(paths)
    click.secho(json_module.dumps(dp.descriptor, indent=4), file=output)
    exit(dp.valid)