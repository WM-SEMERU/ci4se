def get_model(self):
    if self.minisat and self.status == True:
        model = pysolvers.minisatgh_model(self.minisat)
        return model if model != None else []