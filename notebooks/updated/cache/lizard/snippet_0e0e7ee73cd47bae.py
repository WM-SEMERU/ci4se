def current_fact_index(self):
    facts_ids = [fact.id for fact in self.facts]
    return facts_ids.index(self.current_fact.id)