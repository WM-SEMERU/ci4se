def down_ec2(connection, instance_id, region, log=False):
    instance = connection.stop_instances(instance_ids=instance_id)[0]
    while instance.state != 'stopped':
        if log:
            log_yellow('Instance state: %s' % instance.state)
        sleep(10)
        instance.update()
    if log:
        log_green('Instance state: %s' % instance.state)