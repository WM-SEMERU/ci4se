def emit_containers(self, containers, verbose=True):
    containers = sorted(containers, key=lambda c: c.get('name'))
    task_definition = {'family': self.family, 'containerDefinitions':
        containers, 'volumes': self.volumes or []}
    if verbose:
        return json.dumps(task_definition, indent=4, sort_keys=True)
    else:
        return json.dumps(task_definition)