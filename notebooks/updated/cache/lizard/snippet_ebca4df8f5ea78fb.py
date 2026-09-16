def store_meta_data(self, copy_path=None):
    super(ContainerStateModel, self).store_meta_data(copy_path)
    for state_key, state in self.states.items():
        state.store_meta_data(copy_path)