def mon_status_check(conn, logger, hostname, args):
    asok_path = paths.mon.asok(args.cluster, hostname)
    out, err, code = remoto.process.check(conn, ['ceph',
        '--cluster={cluster}'.format(cluster=args.cluster),
        '--admin-daemon', asok_path, 'mon_status'])
    for line in err:
        logger.error(line)
    try:
        return json.loads(b''.join(out).decode('utf-8'))
    except ValueError:
        return {}