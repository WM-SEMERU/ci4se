def start(self, execution_history, backward_execution=False,
    generate_run_id=True):
    self.execution_history = execution_history
    if generate_run_id:
        self._run_id = run_id_generator()
    self.backward_execution = copy.copy(backward_execution)
    self.thread = threading.Thread(target=self.run)
    self.thread.start()