def get_tags_by_fact_id(self, fact_id):
    if not fact_id in self.all_facts_id:
        raise NoHamsterData('facts', fact_id)
    query = 'SELECT tag_id FROM fact_tags WHERE fact_id = %s'
    return [self.tags[row[0]] for row in self._query(query % fact_id)]