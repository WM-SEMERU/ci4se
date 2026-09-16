def output_aliases(aliases):
    for alias in aliases:
        cmd = '!legit ' + alias
        click.echo(columns([colored.yellow('git ' + alias), 20], [cmd, None]))