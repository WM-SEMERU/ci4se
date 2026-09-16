def unregister(self, *model_list):
    for model in model_list:
        if model not in self.registry:
            raise NotRegistered('The model %s is not registered' % model.
                __name__)
        del self.registry[model]