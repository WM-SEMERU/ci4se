def get_component_list_from_workers(self, worker_metadatas):
    comp_list = []
    for platform in sorted(worker_metadatas.keys()):
        for instance in worker_metadatas[platform]['output']:
            if instance['type'] == 'docker-image':
                if 'components' not in instance or not instance['components']:
                    self.log.warn(
                        "Missing 'components' key in 'output' metadata instance: %s"
                        , instance)
                    continue
                comp_list.append(instance['components'])
    return comp_list