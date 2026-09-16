def __create_orget_address(conn, name, region):
    try:
        addy = conn.ex_get_address(name, region)
    except ResourceNotFoundError:
        addr_kwargs = {'name': name, 'region': region}
        new_addy = create_address(addr_kwargs, 'function')
        addy = conn.ex_get_address(new_addy['name'], new_addy['region'])
    return addy