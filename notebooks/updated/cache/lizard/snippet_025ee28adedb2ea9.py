def write_to_file(self, path, filename, footer=True):
    self.filename = filename
    if footer is True:
        _generate_footer(self.notebook, self.notebook_type)
    self.notebook['cells'].append(nb.v4.new_markdown_cell(AUX_CODE_MESSAGE,
        **{'metadata': {'tags': ['hide_mark']}}))
    self.notebook['cells'].append(nb.v4.new_code_cell(CSS_STYLE_CODE, **{
        'metadata': {'tags': ['hide_both']}}))
    self.notebook['cells'].append(nb.v4.new_code_cell(JS_CODE_AUTO_PLAY, **
        {'metadata': {'tags': ['hide_both']}}))
    full_path = (path + '\\Categories\\' + self.notebook_type + '\\' +
        filename + '.ipynb')
    nb.write(self.notebook, full_path)
    os.system(
        'jupyter nbconvert --execute --inplace --ExecutePreprocessor.timeout=-1 '
         + full_path)
    os.system('jupyter trust ' + full_path)