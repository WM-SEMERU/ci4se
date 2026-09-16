def _generate_footer(notebook_object, notebook_type):
    footer_aux = FOOTER
    if 'Main_Files' in notebook_type:
        footer_aux = footer_aux.replace('../MainFiles/', '')
    notebook_object['cells'].append(nb.v4.new_markdown_cell(footer_aux, **{
        'metadata': {'tags': ['footer']}}))
    notebook_object['cells'].append(nb.v4.new_markdown_cell(
        AUX_CODE_MESSAGE, **{'metadata': {'tags': ['hide_mark']}}))
    notebook_object['cells'].append(nb.v4.new_code_cell(CSS_STYLE_CODE, **{
        'metadata': {'tags': ['hide_both']}}))