def result_group_cached(group_id, failures=False, wait=0, count=None,
    broker=None):
    if not broker:
        broker = get_broker()
    start = time()
    if count:
        while True:
            if count_group_cached(group_id) == count or wait and (time() -
                start) * 1000 >= wait > 0:
                break
            sleep(0.01)
    while True:
        group_list = broker.cache.get('{}:{}:keys'.format(broker.list_key,
            group_id))
        if group_list:
            result_list = []
            for task_key in group_list:
                task = SignedPackage.loads(broker.cache.get(task_key))
                if task['success'] or failures:
                    result_list.append(task['result'])
            return result_list
        if (time() - start) * 1000 >= wait >= 0:
            break
        sleep(0.01)