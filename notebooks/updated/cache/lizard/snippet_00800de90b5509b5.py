def classify_field(value):
    if not (isinstance(value, six.string_types) and value):
        return
    schema = load_schema('elements/inspire_field')
    inspire_categories = schema['properties']['term']['enum']
    for inspire_category in inspire_categories:
        if value.upper() == inspire_category.upper():
            return inspire_category
    category = normalize_arxiv_category(value)
    return ARXIV_TO_INSPIRE_CATEGORY_MAPPING.get(category, 'Other')