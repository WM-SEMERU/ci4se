def cluster_list(verbose=False):
    cmd = [salt.utils.path.which('pg_lsclusters'), '--no-header']
    ret = __salt__['cmd.run_all'](' '.join([pipes.quote(c) for c in cmd]))
    if ret.get('retcode', 0) != 0:
        log.error('Error listing clusters')
    cluster_dict = _parse_pg_lscluster(ret['stdout'])
    if verbose:
        return cluster_dict
    return cluster_dict.keys()