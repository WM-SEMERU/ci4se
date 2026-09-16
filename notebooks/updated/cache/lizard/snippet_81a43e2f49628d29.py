def get_concept_item_mapping(self, concepts=None, lang=None):
    if concepts is None:
        concepts = self.filter(active=True)
        if lang is not None:
            concepts = concepts.filter(lang=lang)
    if lang is None:
        languages = set([concept.lang for concept in concepts])
        if len(languages) > 1:
            raise Exception('Concepts has multiple languages')
        lang = list(languages)[0]
    item_lists = Item.objects.filter_all_reachable_leaves_many([json.loads(
        concept.query) for concept in concepts], lang)
    return dict(zip([c.pk for c in concepts], item_lists))