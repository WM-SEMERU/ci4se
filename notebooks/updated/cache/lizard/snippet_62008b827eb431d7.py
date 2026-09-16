def clean(self, initial_epoch):
    self.db.metrics.delete_many({'run_name': self.model_config.run_name,
        'epoch_idx': {'$gt': initial_epoch}})