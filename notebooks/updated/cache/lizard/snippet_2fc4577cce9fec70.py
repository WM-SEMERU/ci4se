def Containers(vent=True, running=True, exclude_labels=None):
    containers = []
    try:
        d_client = docker.from_env()
        if vent:
            c = d_client.containers.list(all=not running, filters={'label':
                'vent'})
        else:
            c = d_client.containers.list(all=not running)
        for container in c:
            include = True
            if exclude_labels:
                for label in exclude_labels:
                    if ('vent.groups' in container.labels and label in
                        container.labels['vent.groups']):
                        include = False
            if include:
                containers.append((container.name, container.status))
    except Exception as e:
        logger.error('Docker problem ' + str(e))
    return containers