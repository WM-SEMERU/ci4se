def compute_media_queries(element):
    parent_glossary = element.get_parent_glossary()
    element.glossary['container_max_widths'] = max_widths = {}
    element.glossary['media_queries'] = media_queries = {}
    breakpoints = element.glossary.get('breakpoints', parent_glossary.get(
        'breakpoints', []))
    last_index = len(breakpoints) - 1
    fluid = element.glossary.get('fluid')
    for index, bp in enumerate(breakpoints):
        try:
            key = ('container_fluid_max_widths' if fluid else
                'container_max_widths')
            max_widths[bp] = parent_glossary[key][bp]
        except KeyError:
            max_widths[bp] = BS3_BREAKPOINTS[bp][4 if fluid else 3]
        if last_index > 0:
            if index == 0:
                next_bp = breakpoints[1]
                media_queries[bp] = ['(max-width: {0}px)'.format(
                    BS3_BREAKPOINTS[next_bp][0])]
            elif index == last_index:
                media_queries[bp] = ['(min-width: {0}px)'.format(
                    BS3_BREAKPOINTS[bp][0])]
            else:
                next_bp = breakpoints[index + 1]
                media_queries[bp] = ['(min-width: {0}px)'.format(
                    BS3_BREAKPOINTS[bp][0]), '(max-width: {0}px)'.format(
                    BS3_BREAKPOINTS[next_bp][0])]