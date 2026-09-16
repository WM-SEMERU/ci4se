def get_core(self):
    if self.glucose and self.status == False:
        return pysolvers.glucose3_core(self.glucose)