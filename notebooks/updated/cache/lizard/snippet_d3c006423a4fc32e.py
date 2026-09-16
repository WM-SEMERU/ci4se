def get_ceph_pools(self, sentry_unit):
    pools = {}
    cmd = 'sudo ceph osd lspools'
    output, code = sentry_unit.run(cmd)
    if code != 0:
        msg = '{} `{}` returned {} {}'.format(sentry_unit.info['unit_name'],
            cmd, code, output)
        amulet.raise_status(amulet.FAIL, msg=msg)
    output = output.replace('\n', ',')
    for pool in str(output).split(','):
        pool_id_name = pool.split(' ')
        if len(pool_id_name) == 2:
            pool_id = pool_id_name[0]
            pool_name = pool_id_name[1]
            pools[pool_name] = int(pool_id)
    self.log.debug('Pools on {}: {}'.format(sentry_unit.info['unit_name'],
        pools))
    return pools