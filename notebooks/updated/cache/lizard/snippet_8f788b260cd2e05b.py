def allocation(node, format, h):
    try:
        response = base.es.cat.allocation(node_id=node, bytes=format, h=h,
            format='json')
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table)