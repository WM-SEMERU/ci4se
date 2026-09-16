def _year_month_delta_from_elements(elements):
    return divmod(int(elements.get('years', 0)) * MONTHS_IN_YEAR + elements
        .get('months', 0), MONTHS_IN_YEAR)