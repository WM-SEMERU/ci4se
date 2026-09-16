def initialize_worker(self, process_num=None):
    self.initial_state.process = process_num
    self.random.seed(hash(self.seed) + hash(process_num))