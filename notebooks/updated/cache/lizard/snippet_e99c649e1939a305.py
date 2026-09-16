def relieve_all_models(self):
    map(self.relieve_model, list(self.__registered_models))
    self.__registered_models.clear()