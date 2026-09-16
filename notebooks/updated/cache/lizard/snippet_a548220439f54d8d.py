def build_rectangle_dict(self, north, west, south, east, stroke_color=
    '#FF0000', stroke_opacity=0.8, stroke_weight=2, fill_color='#FF0000',
    fill_opacity=0.3):
    rectangle = {'stroke_color': stroke_color, 'stroke_opacity':
        stroke_opacity, 'stroke_weight': stroke_weight, 'fill_color':
        fill_color, 'fill_opacity': fill_opacity, 'bounds': {'north': north,
        'west': west, 'south': south, 'east': east}}
    return rectangle