def update_house(self, complex: str, id: str, **kwargs):
    self.check_house(complex, id)
    self.put('developers/{developer}/complexes/{complex}/houses/{id}'.
        format(developer=self.developer, complex=complex, id=id), data=kwargs)