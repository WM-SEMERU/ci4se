def init_all_objects(self, data, target=None, single_result=True):
    if single_result:
        return self.init_target_object(target, data)
    return list(self.expand_models(target, data))