def get_keys(self, lst):
    pk_name = self.get_pk_name()
    return [getattr(item, pk_name) for item in lst]