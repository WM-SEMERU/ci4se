def delete_ipv4_range(start_addr=None, end_addr=None, **api_opts):
    r = get_ipv4_range(start_addr, end_addr, **api_opts)
    if r:
        return delete_object(r['_ref'], **api_opts)
    else:
        return True