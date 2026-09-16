def require(*reqs):
    for req in reqs:
        if type(req) is str:
            if not os.path.exists(req) and req not in GENERATES:
                abort(LOCALE['abort_bad_file'].format(req))
            if req not in GENERATES:
                return
            if req in GENERATES:
                req = GENERATES[req]
        if req.valid is None:
            if len(req.args):
                abort(LOCALE['abort_bad_args'], req, len(req.args))
            req()
        if req.valid is False:
            abort(LOCALE['abort_bad_task'], req)