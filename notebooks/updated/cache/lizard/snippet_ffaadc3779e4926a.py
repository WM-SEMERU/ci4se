def post_mortem(tb=None, host='', port=5555, patch_stdstreams=False):
    if tb is None:
        t, v, tb = sys.exc_info()
        exc_data = traceback.format_exception(t, v, tb)
    else:
        exc_data = traceback.format_tb(tb)
    if tb is None:
        raise ValueError(
            'A valid traceback must be passed if no exception is being handled'
            )
    pdb = WebPdb.active_instance
    if pdb is None:
        pdb = WebPdb(host, port, patch_stdstreams)
    else:
        pdb.remove_trace()
    pdb.console.writeline('*** Web-PDB post-mortem ***\n')
    pdb.console.writeline(''.join(exc_data))
    pdb.reset()
    pdb.interaction(None, tb)