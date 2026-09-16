def _pre_train(self, stop_param_updates, num_epochs, updates_epoch):
    updates = {k: (stop_param_updates.get(k, num_epochs) * updates_epoch) for
        k, v in self.params.items()}
    single_steps = {k: np.exp(-(1.0 - 1.0 / v) * self.params[k]['factor']) for
        k, v in updates.items()}
    constants = {k: (np.exp(-self.params[k]['factor']) / v) for k, v in
        single_steps.items()}
    return constants