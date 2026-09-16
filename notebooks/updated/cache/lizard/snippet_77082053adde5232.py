def translate_identifiers(self, identifiers, language):
    result = {}
    identifiers = set(identifiers)
    item_types = ItemType.objects.get_all_types()
    for item_type_id, type_identifiers in proso.list.group_by(identifiers,
        by=lambda identifier: self.get_item_type_id_from_identifier(
        identifier, item_types)).items():
        to_find = {}
        for identifier in type_identifiers:
            identifier_split = identifier.split('/')
            to_find[identifier_split[1]] = identifier
        kwargs = {'identifier__in': list(to_find.keys())}
        item_type = ItemType.objects.get_all_types()[item_type_id]
        model = ItemType.objects.get_model(item_type_id)
        if 'language' in item_type:
            kwargs[item_type['language']] = language
        for identifier, item_id in model.objects.filter(**kwargs).values_list(
            'identifier', item_type['foreign_key']):
            result[to_find[identifier]] = item_id
    if len(result) != len(identifiers):
        raise HttpError(404,
            "Can't translate the following identifiers: {}".format(set(
            identifiers) - set(result.keys())), 'identifier_not_found')
    return result