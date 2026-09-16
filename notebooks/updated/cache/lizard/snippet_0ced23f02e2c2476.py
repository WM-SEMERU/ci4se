def _get_theme_label(catalog, theme):
    try:
        label = catalog.get_theme(identifier=theme)['label']
    except BaseException:
        try:
            label = catalog.get_theme(label=theme)['label']
        except BaseException:
            raise ce.ThemeNonExistentError(theme)
    label = re.sub('[^\\wá-úÁ-ÚñÑ .-]+', '', label, flags=re.UNICODE)
    return label