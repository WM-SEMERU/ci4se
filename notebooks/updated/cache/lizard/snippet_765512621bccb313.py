def _get_projection(el):
    result = None
    if hasattr(el, 'crs'):
        result = int(el._auxiliary_component), el.crs
    return result