def meth_wdl(args):
    r = fapi.get_repository_method(args.namespace, args.method, args.
        snapshot_id, True)
    fapi._check_response_code(r, 200)
    return r.text