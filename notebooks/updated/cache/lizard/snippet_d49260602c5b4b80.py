def get_departments_by_college(college):
    url = '{}?{}'.format(dept_search_url_prefix, urlencode({
        'college_abbreviation': college.label}))
    return _json_to_departments(get_resource(url), college)