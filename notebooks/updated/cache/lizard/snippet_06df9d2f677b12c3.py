def split_css_classes(css_classes):
    classes_list = text_value(css_classes).split(' ')
    return [c for c in classes_list if c]