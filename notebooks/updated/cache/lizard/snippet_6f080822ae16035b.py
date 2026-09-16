def add_line(preso, x1, y1, x2, y2, width='3pt', color='red'):
    marker_end_ratio = 0.459 / 3
    marker_start_ratio = 0.359 / 3
    stroke_ratio = 0.106 / 3
    w = float(width[0:width.index('pt')])
    sw = w * stroke_ratio
    mew = w * marker_end_ratio
    msw = w * marker_start_ratio
    attribs = {'svg:stroke-width': '{}cm'.format(sw), 'svg:stroke-color':
        color, 'draw:marker-start-width': '{}cm'.format(msw),
        'draw:marker-end': 'Arrow', 'draw:marker-end-width': '{}cm'.format(
        mew), 'draw:fill': 'none', 'draw:textarea-vertical-align': 'middle'}
    style = LineStyle(**attribs)
    preso.add_style(style)
    line_attrib = {'draw:style-name': style.name, 'draw:layer': 'layout',
        'svg:x1': x1, 'svg:y1': y1, 'svg:x2': x2, 'svg:y2': y2}
    line_node = el('draw:line', attrib=line_attrib)
    preso.slides[-1]._page.append(line_node)