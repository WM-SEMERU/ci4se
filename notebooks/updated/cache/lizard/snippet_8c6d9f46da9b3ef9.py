def get_core(self):
    if self.maplesat and self.status == False:
        return pysolvers.maplecm_core(self.maplesat)