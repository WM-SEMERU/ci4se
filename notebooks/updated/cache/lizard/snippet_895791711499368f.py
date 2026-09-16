def parse_string(self, string, best=False):
    if isinstance(string, list):
        items = string
    else:
        items = string.split()
    item_list = []
    not_next = False
    for item in items:
        if self.negative:
            if item == 'not':
                not_next = True
                continue
            if item[0] == '-':
                not_next = True
                item = item[1:]
        concepts = self.match_all_concepts(item)
        if len(concepts) > 0:
            if not_next:
                for concept in concepts:
                    concept.negative = True
            if best:
                item_list.append(concepts[0])
            else:
                item_list.append(concepts)
        else:
            item_list.append(item)
        not_next = False
    return item_list