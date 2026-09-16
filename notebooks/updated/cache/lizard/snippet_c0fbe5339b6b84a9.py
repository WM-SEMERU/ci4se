def get_repository(self, entity_cls):
    model_cls = self.get_model(entity_cls)
    return DictRepository(self, entity_cls, model_cls)