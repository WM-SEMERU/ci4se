def visit_variants(self, func, variants=None, **kwargs):
    if variants:
        present_variants = range(self.package.num_variants)
        invalid_variants = set(variants) - set(present_variants)
        if invalid_variants:
            raise BuildError(
                'The package does not contain the variants: %s' % ', '.join
                (str(x) for x in sorted(invalid_variants)))
    results = []
    num_visited = 0
    for variant in self.package.iter_variants():
        if variants and variant.index not in variants:
            self._print_header('Skipping variant %s (%s)...' % (variant.
                index, self._n_of_m(variant)))
            continue
        result = func(variant, **kwargs)
        results.append(result)
        num_visited += 1
    return num_visited, results