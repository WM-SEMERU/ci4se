def base_name_from_image(image):
    m = re.match('^(.+/)?([^:/]+)(:[^:]+)?$', image)
    algo_name = m.group(2) if m else image
    return algo_name