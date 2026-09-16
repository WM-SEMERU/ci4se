def check_siblings(graph, outputs):
    siblings = set()
    for node in outputs:
        siblings |= graph.siblings(node)
    siblings = {node.path for node in siblings}
    missing = siblings - {node.path for node in outputs}
    if missing:
        msg = (
            'Include the files above in the command or use the --with-siblings option.'
            )
        raise click.ClickException(
            'There are missing output siblings:\n\n\t{0}\n\n{1}'.format(
            '\n\t'.join(click.style(path, fg='red') for path in missing), msg))
    return outputs