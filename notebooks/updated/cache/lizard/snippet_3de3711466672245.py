def add_reaction(self, reaction_id):
    if reaction_id in self._reaction_set:
        return
    reaction = self._database.get_reaction(reaction_id)
    self._reaction_set.add(reaction_id)
    for compound, _ in reaction.compounds:
        self._compound_set.add(compound)