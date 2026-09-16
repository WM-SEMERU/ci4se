def get_core(self):
    if self.maplesat and self.status == False:
        return pysolvers.maplesat_core(self.maplesat)