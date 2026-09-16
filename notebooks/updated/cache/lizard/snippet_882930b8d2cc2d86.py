def add_clause(self, clause, no_return=True):
    if self.glucose:
        res = pysolvers.glucose3_add_cl(self.glucose, clause)
        if res == False:
            self.status = False
        if not no_return:
            return res