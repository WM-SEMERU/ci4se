def new(self, bootstrap_with=None, use_timer=False, with_proof=False):
    if not self.maplesat:
        self.maplesat = pysolvers.maplesat_new()
        if bootstrap_with:
            for clause in bootstrap_with:
                self.add_clause(clause)
        self.use_timer = use_timer
        self.call_time = 0.0
        self.accu_time = 0.0
        if with_proof:
            self.prfile = tempfile.TemporaryFile()
            pysolvers.maplesat_tracepr(self.maplesat, self.prfile)