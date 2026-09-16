def solve(self, assumptions=[]):
    if self.lingeling:
        if self.use_timer:
            start_time = time.clock()
        def_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.status = pysolvers.lingeling_solve(self.lingeling, assumptions)
        def_sigint_handler = signal.signal(signal.SIGINT, def_sigint_handler)
        if self.use_timer:
            self.call_time = time.clock() - start_time
            self.accu_time += self.call_time
        self.prev_assumps = assumptions
        return self.status