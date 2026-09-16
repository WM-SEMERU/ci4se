def _save_params(self):
    self.model.save_params_to_file(self.current_params_fname)
    utils.cleanup_params_files(self.model.output_dir, self.
        max_params_files_to_keep, self.state.checkpoint, self.state.
        best_checkpoint, self.keep_initializations)