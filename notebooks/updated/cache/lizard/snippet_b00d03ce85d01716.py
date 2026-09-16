def get_min_isr(zk, topic):
    ISR_CONF_NAME = 'min.insync.replicas'
    try:
        config = zk.get_topic_config(topic)
    except NoNodeError:
        return None
    if ISR_CONF_NAME in config['config']:
        return int(config['config'][ISR_CONF_NAME])
    else:
        return None