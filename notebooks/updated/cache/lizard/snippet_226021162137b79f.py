def _checkpoint_trial_if_needed(self, trial):
    if trial.should_checkpoint():
        if hasattr(trial, 'runner') and trial.runner:
            self.trial_executor.save(trial, storage=Checkpoint.DISK)
        self.trial_executor.try_checkpoint_metadata(trial)