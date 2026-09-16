def add_model(self, model):
    logger.debug('adding model {} to group {}'.format(model.name, self.name))
    self.models[model.name] = model