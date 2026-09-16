def scale_sections(sections, scaling_scope):
    new_sections = []
    if scaling_scope == 'layer':
        for section in sections:
            new_sections.append(scale_image_for_display(section))
    elif scaling_scope == 'network':
        global_min, global_max = global_extrema(sections)
        for section in sections:
            new_sections.append(scale_image_for_display(section, global_min,
                global_max))
    return new_sections