def install_code_colorscheme(self, name, style_dict):
    assert isinstance(name, six.text_type)
    assert isinstance(style_dict, dict)
    self.code_styles[name] = style_dict