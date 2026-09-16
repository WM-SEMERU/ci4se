def restore(self, checkpoint_path):
    with open(checkpoint_path + '.tune_metadata', 'rb') as f:
        metadata = pickle.load(f)
    self._experiment_id = metadata['experiment_id']
    self._iteration = metadata['iteration']
    self._timesteps_total = metadata['timesteps_total']
    self._time_total = metadata['time_total']
    self._episodes_total = metadata['episodes_total']
    saved_as_dict = metadata['saved_as_dict']
    if saved_as_dict:
        with open(checkpoint_path, 'rb') as loaded_state:
            checkpoint_dict = pickle.load(loaded_state)
        self._restore(checkpoint_dict)
    else:
        self._restore(checkpoint_path)
    self._time_since_restore = 0.0
    self._timesteps_since_restore = 0
    self._iterations_since_restore = 0
    self._restored = True