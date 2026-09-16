def factor_hatch(field_name, patterns, factors, start=0, end=None):
    return field(field_name, CategoricalPatternMapper(patterns=patterns,
        factors=factors, start=start, end=end))