def trigger_all_callbacks(self, callbacks=None):
    return [ret for key in self for ret in self.trigger_callbacks(key,
        callbacks=None)]