def generate(categorize=unicodedata.category, group_class=RangeGroup):
    categories = collections.defaultdict(list)
    last_category = None
    last_range = None
    for c in range(sys.maxunicode + 1):
        category = categorize(chr(c))
        if category != last_category:
            last_category = category
            last_range = [c, c + 1]
            categories[last_category].append(last_range)
        else:
            last_range[1] += 1
    categories = {k: group_class(v) for k, v in categories.items()}
    categories.update({k: merge(*map(categories.__getitem__, g)) for k, g in
        itertools.groupby(sorted(categories), key=lambda k: k[0])})
    return categories