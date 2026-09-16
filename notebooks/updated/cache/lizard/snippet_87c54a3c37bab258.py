def _safe_get_element_date(self, path, root=None):
    value = self._safe_get_element_text(path=path, root=root)
    if value is not None:
        try:
            value = dateutil.parser.parse(value)
            if value:
                value = value.date()
        except ValueError:
            value = None
    return value