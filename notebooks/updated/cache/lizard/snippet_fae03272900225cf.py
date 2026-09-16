def add_named_concept_filters(self, named_filter_concepts):
    for concept_key, concept_name in named_filter_concepts.items():
        self.add_concept_filter(concept_key, concept_name=concept_name)