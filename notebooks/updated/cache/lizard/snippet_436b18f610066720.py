def run(self):

    def compound_name(id):
        if id not in self._model.compounds:
            return id
        return self._model.compounds[id].properties.get('name', id)

    def reaction_genes_string(id):
        if id not in self._model.reactions:
            return ''
        return self._model.reactions[id].properties.get('genes', '')
    reaction = self._get_objective()
    if not self._mm.has_reaction(reaction):
        self.fail('Specified reaction is not in model: {}'.format(reaction))
    loop_removal = self._get_loop_removal_option()
    if loop_removal == 'none':
        result = self.run_fba(reaction)
    elif loop_removal == 'l1min':
        result = self.run_fba_minimized(reaction)
    elif loop_removal == 'tfba':
        result = self.run_tfba(reaction)
    optimum = None
    total_reactions = 0
    nonzero_reactions = 0
    for reaction_id, flux in sorted(result):
        total_reactions += 1
        if abs(flux) > self._args.epsilon:
            nonzero_reactions += 1
        if abs(flux) > self._args.epsilon or self._args.all_reactions:
            rx = self._mm.get_reaction(reaction_id)
            rx_trans = rx.translated_compounds(compound_name)
            genes = reaction_genes_string(reaction_id)
            print('{}\t{}\t{}\t{}'.format(reaction_id, flux, rx_trans, genes))
        if reaction_id == reaction:
            optimum = flux
    logger.info('Objective flux: {}'.format(optimum))
    logger.info('Reactions at zero flux: {}/{}'.format(total_reactions -
        nonzero_reactions, total_reactions))