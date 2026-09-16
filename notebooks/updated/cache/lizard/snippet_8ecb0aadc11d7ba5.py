def order_list(backend, kitchen):
    err_str, use_kitchen = Backend.get_kitchen_from_user(kitchen)
    if use_kitchen is None:
        raise click.ClickException(err_str)
    click.secho('%s - Get Order information for Kitchen %s' % (get_datetime
        (), use_kitchen), fg='green')
    check_and_print(DKCloudCommandRunner.list_order(backend.dki, use_kitchen))