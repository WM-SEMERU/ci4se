def refresh_db(full=False, **kwargs):
    salt.utils.pkg.clear_rtag(__opts__)
    if full:
        return __salt__['cmd.retcode']('/bin/pkg refresh --full') == 0
    else:
        return __salt__['cmd.retcode']('/bin/pkg refresh') == 0