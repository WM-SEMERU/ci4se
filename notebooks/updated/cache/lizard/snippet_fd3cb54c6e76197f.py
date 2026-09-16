def wait_for_stable_cluster(hosts, jolokia_port, jolokia_prefix,
    check_interval, check_count, unhealthy_time_limit):
    stable_counter = 0
    max_checks = int(math.ceil(unhealthy_time_limit / check_interval))
    for i in itertools.count():
        partitions, brokers = read_cluster_status(hosts, jolokia_port,
            jolokia_prefix)
        if partitions or brokers:
            stable_counter = 0
        else:
            stable_counter += 1
        print(
            'Under replicated partitions: {p_count}, missing brokers: {b_count} ({stable}/{limit})'
            .format(p_count=partitions, b_count=brokers, stable=
            stable_counter, limit=check_count))
        if stable_counter >= check_count:
            print('The cluster is stable')
            return
        if i >= max_checks:
            raise WaitTimeoutException()
        time.sleep(check_interval)