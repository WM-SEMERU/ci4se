def _compute_next_evaluations(self, pending_zipped_X=None, ignored_zipped_X
    =None):
    self.acquisition.optimizer.context_manager = ContextManager(self.space,
        self.context)
    if self.de_duplication:
        duplicate_manager = DuplicateManager(space=self.space, zipped_X=
            self.X, pending_zipped_X=pending_zipped_X, ignored_zipped_X=
            ignored_zipped_X)
    else:
        duplicate_manager = None
    return self.space.zip_inputs(self.evaluator.compute_batch(
        duplicate_manager=duplicate_manager, context_manager=self.
        acquisition.optimizer.context_manager))