def export(outfile, pk):
    load_dbenv_if_not_loaded()
    from aiida.orm import load_node
    node = load_node(pk)
    string = str(node)
    if outfile:
        with open(outfile, 'w') as f:
            f.write(string)
    else:
        click.echo(string)