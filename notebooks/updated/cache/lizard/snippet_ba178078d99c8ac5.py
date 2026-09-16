def get_core(self):
    if self.maplesat and self.status == False:
        return pysolvers.maplechrono_core(self.maplesat)