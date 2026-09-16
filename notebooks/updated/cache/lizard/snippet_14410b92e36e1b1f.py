def get_related_synsets(self, relation):
    results = []
    for relation_candidate in self._raw_synset.internalLinks:
        if relation_candidate.name == relation:
            linked_synset = synset(_get_key_from_raw_synset(
                relation_candidate.target_concept))
            relation_candidate.target_concept = linked_synset._raw_synset
            results.append(linked_synset)
    return results