def GetUnreachableInstances(instances, ssh_key):
    hostnames = [i.private_ip for i in instances]
    ssh_status = AreHostsReachable(hostnames, ssh_key)
    assert len(hostnames) == len(ssh_status)
    nonresponsive_instances = [instance for instance, ssh_ok in zip(
        instances, ssh_status) if not ssh_ok]
    return nonresponsive_instances