def load(self, cls, run_id):
    id_code = self.generate_load_identifier(cls, run_id)
    inst = self.store.load(id_code)
    return inst