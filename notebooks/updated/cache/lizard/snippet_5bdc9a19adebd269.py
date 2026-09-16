def _font_name(self, ufo):
    family_name = ufo.info.familyName.replace(' ', ''
        ) if ufo.info.familyName is not None else 'None'
    style_name = ufo.info.styleName.replace(' ', ''
        ) if ufo.info.styleName is not None else 'None'
    return '{}-{}'.format(family_name, style_name)