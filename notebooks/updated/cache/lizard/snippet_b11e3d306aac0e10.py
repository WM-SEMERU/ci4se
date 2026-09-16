def cli(ctx):
    current_version = get_distribution('apio').version
    latest_version = get_pypi_latest_version()
    if latest_version is None:
        ctx.exit(1)
    if latest_version == current_version:
        click.secho(
            "You're up-to-date!\nApio {} is currently the newest version available."
            .format(latest_version), fg='green')
    else:
        click.secho(
            "You're not updated\nPlease execute `pip install -U apio` to upgrade."
            , fg='yellow')