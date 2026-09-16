def register(self, model, related=None):
    update_model = UpdateSE(self, related)
    self.REGISTERED_MODELS[model] = update_model
    self.router.post_commit.bind(update_model, model)
    self.router.post_delete.bind(update_model, model)