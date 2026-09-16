def get_sections_by_curriculum_and_term(curriculum, term):
    url = '{}?{}'.format(section_res_url_prefix, urlencode([(
        'curriculum_abbreviation', curriculum.label), ('quarter', term.
        quarter.lower()), ('year', term.year)]))
    return _json_to_sectionref(get_resource(url))