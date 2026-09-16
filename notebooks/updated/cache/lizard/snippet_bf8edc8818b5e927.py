def _initialize_cfg(self):
    self.kb.functions = FunctionManager(self.kb)
    self._jobs_to_analyze_per_function = defaultdict(set)
    self._completed_functions = set()