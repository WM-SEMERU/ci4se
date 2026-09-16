def get_service_ips(service_name, task_name=None, inactive=False, completed
    =False):
    service_tasks = get_service_tasks(service_name, inactive, completed)
    ips = set([])
    for task in service_tasks:
        if task_name is None or task['name'] == task_name:
            for status in task['statuses']:
                if status['state'] != 'TASK_RUNNING':
                    continue
                for ip in status['container_status']['network_infos'][0][
                    'ip_addresses']:
                    ips.add(ip['ip_address'])
    return ips