def _folder_item_specifications(self, analysis_brain, item):
    item['Specification'] = ''
    results_range = analysis_brain.getResultsRange
    if not results_range:
        return
    item['Specification'] = get_formatted_interval(results_range, '')
    out_range, out_shoulders = is_out_of_range(analysis_brain)
    if not out_range:
        return
    img = get_image('exclamation.png', title=_('Result out of range'))
    if not out_shoulders:
        img = get_image('warning.png', title=_('Result in shoulder range'))
    self._append_html_element(item, 'Result', img)