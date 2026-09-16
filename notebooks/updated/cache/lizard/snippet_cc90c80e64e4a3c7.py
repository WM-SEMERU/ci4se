def check_environment_presets():
    presets = [x for x in os.environ.copy().keys() if x.startswith('NOVA_') or
        x.startswith('OS_')]
    if len(presets) < 1:
        return True
    else:
        click.echo('_' * 80)
        click.echo(
            '*WARNING* Found existing environment variables that may cause conflicts:'
            )
        for preset in presets:
            click.echo('  - %s' % preset)
        click.echo('_' * 80)
        return False