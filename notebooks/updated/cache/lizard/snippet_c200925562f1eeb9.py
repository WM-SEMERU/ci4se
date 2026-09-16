def start(**kwargs):
    output, err = cli_syncthing_adapter.start(**kwargs)
    click.echo('%s' % output, err=err)