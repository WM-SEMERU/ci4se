def live_dirs(self):
    if self.has_results_dir:
        yield self.results_dir
        yield self.current_results_dir
        if self.has_previous_results_dir:
            yield self.previous_results_dir