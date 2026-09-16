def cli(inputtiles, delimiter):
    try:
        inputtiles = click.open_file(inputtiles).readlines()
    except IOError:
        inputtiles = [inputtiles]
    for x in xt.xvert(inputtiles, delimiter):
        click.echo(x)