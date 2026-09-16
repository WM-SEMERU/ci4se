def set_contourf_properties(stroke_width, fcolor, fill_opacity,
    contour_levels, contourf_idx, unit):
    return {'stroke': fcolor, 'stroke-width': stroke_width,
        'stroke-opacity': 1, 'fill': fcolor, 'fill-opacity': fill_opacity,
        'title': '%.2f' % contour_levels[contourf_idx] + ' ' + unit}