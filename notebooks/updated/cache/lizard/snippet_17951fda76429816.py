def _helper_for_model(self, model_type):
    if model_type is models.containers.Container:
        return self.containers
    if model_type is models.images.Image:
        return self.images
    if model_type is models.networks.Network:
        return self.networks
    if model_type is models.volumes.Volume:
        return self.volumes
    raise ValueError('Unknown model type {}'.format(model_type))