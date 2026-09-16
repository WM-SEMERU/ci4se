def update(self, container, instances=None, map_name=None, **kwargs):
    return self.run_actions('update', container, instances=instances,
        map_name=map_name, **kwargs)