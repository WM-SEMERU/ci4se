def _compute_quads(self, element, data, mapping):
    quad_mapping = {'left': 'x0', 'right': 'x1', 'bottom': 'y0', 'top': 'y1'}
    quad_data = dict(data['scatter_1'])
    quad_data.update({'x0': [], 'x1': [], 'y0': [], 'y1': []})
    for node in element._sankey['nodes']:
        quad_data['x0'].append(node['x0'])
        quad_data['y0'].append(node['y0'])
        quad_data['x1'].append(node['x1'])
        quad_data['y1'].append(node['y1'])
        data['scatter_1'].update(quad_data)
    data['quad_1'] = data['scatter_1']
    mapping['quad_1'] = quad_mapping