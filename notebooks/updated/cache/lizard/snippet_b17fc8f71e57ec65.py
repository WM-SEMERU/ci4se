def match_country_name_to_its_code(country_name, city=''):
    if country_name:
        country_name = country_name.upper().replace('.', '').strip()
        if country_to_iso_code.get(country_name):
            return country_to_iso_code.get(country_name)
        elif country_name == 'KOREA':
            if city.upper() in south_korean_cities:
                return 'KR'
        else:
            for c_code, spellings in countries_alternative_spellings.items():
                for spelling in spellings:
                    if country_name == spelling:
                        return c_code
    return None