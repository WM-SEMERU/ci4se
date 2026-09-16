def find_txt(xml_tree, path, default=''):
    value = ''
    try:
        xpath_applied = xml_tree.xpath(path)
        if len(xpath_applied) and xpath_applied[0] is not None:
            xpath_result = xpath_applied[0]
            if isinstance(xpath_result, type(xml_tree)):
                value = xpath_result.text.strip()
            else:
                value = xpath_result
    except Exception:
        value = default
    return py23_compat.text_type(value)