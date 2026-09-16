def add_chain_ids(self, chains):
    chains = ssbio.utils.force_list(chains)
    for c in chains:
        if self.chains.has_id(c):
            log.debug('{}: chain already present'.format(c))
        else:
            chain_prop = ChainProp(ident=c, pdb_parent=self.id)
            self.chains.append(chain_prop)
            log.debug('{}: added to chains list'.format(c))