def _create_tooltips(hist: Histogram1D, vega: dict, kwargs: dict):
    if kwargs.pop('tooltips', False):
        vega['signals'] = vega.get('signals', [])
        vega['signals'].append({'name': 'tooltip', 'value': {}, 'on': [{
            'events': 'rect:mouseover', 'update': 'datum'}, {'events':
            'rect:mouseout', 'update': '{}'}]})
        font_size = kwargs.get('fontsize', DEFAULT_FONTSIZE)
        vega['marks'] = vega.get('marks', [])
        vega['marks'].append({'type': 'text', 'encode': {'enter': {'align':
            {'value': 'center'}, 'baseline': {'value': 'bottom'}, 'fill': {
            'value': '#333'}, 'fontSize': {'value': font_size}}, 'update':
            {'x': {'scale': 'xscale', 'signal':
            '(tooltip.x + tooltip.x2) / 2', 'band': 0.5}, 'y': {'scale':
            'yscale', 'signal': 'tooltip.y', 'offset': -2}, 'text': {
            'signal': 'tooltip.y'}, 'fillOpacity': [{'test':
            'datum === tooltip', 'value': 0}, {'value': 1}]}}})