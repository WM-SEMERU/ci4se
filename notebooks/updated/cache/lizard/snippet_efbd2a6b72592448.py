def _compute_subplot_domains(widths, spacing):
    widths_sum = float(sum(widths))
    total_spacing = (len(widths) - 1) * spacing
    widths = [(w / widths_sum * (1 - total_spacing)) for w in widths]
    domains = []
    for c in range(len(widths)):
        domain_start = c * spacing + sum(widths[:c])
        domain_stop = min(1, domain_start + widths[c])
        domains.append((domain_start, domain_stop))
    return domains