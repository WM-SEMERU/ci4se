def set_context(self, cell_type):
    if self.model is None:
        return
    monomer_names = [m.name for m in self.model.monomers]
    res = context_client.get_protein_expression(monomer_names, [cell_type])
    amounts = res.get(cell_type)
    if not amounts:
        logger.warning('Could not get context for %s cell type.' % cell_type)
        self.add_default_initial_conditions()
        return
    self.set_expression(amounts)