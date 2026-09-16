def rmq_wait_for_cluster(self, deployment, init_sleep=15, timeout=1200):
    if init_sleep:
        time.sleep(init_sleep)
    message = re.compile('^Unit is ready and clustered$')
    deployment._auto_wait_for_status(message=message, timeout=timeout,
        include_only=['rabbitmq-server'])