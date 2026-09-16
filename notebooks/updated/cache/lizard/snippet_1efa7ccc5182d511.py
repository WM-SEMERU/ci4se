def load_styles(path_or_doc):
    if isinstance(path_or_doc, string_types):
        doc = load(path_or_doc)
    else:
        if isinstance(path_or_doc, ODFDocument):
            doc = path_or_doc._doc
        else:
            doc = path_or_doc
        assert isinstance(doc, OpenDocument), doc
    styles = {_style_name(style): style for style in doc.styles.childNodes}
    return styles