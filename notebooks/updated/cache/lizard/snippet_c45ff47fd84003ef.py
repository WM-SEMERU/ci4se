def load(manager, units=80):
    pb_connecting = manager.counter(total=units, desc='Loading', unit=
        'services', color='red', bar_format=BAR_FMT)
    pb_loading = pb_connecting.add_subcounter('yellow')
    pb_loaded = pb_connecting.add_subcounter('green', all_fields=True)
    connecting = []
    loading = []
    loaded = []
    count = 0
    while pb_loaded.count < units:
        time.sleep(random.uniform(0.05, 0.15))
        for idx, node in enumerate(loading):
            if node.loaded:
                loading.pop(idx)
                loaded.append(node)
                LOGGER.info('Service %d loaded', node.iden)
                pb_loaded.update_from(pb_loading)
        for idx, node in enumerate(connecting):
            if node.connected:
                connecting.pop(idx)
                node.load()
                loading.append(node)
                LOGGER.info('Service %d connected', node.iden)
                pb_loading.update_from(pb_connecting)
        for _ in range(0, min(units - count, 5 - len(connecting))):
            node = Node(count)
            node.connect()
            connecting.append(node)
            LOGGER.info('Connection to service %d', node.iden)
            pb_connecting.update()
            count += 1