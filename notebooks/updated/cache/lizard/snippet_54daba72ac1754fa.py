def input_classes(self):
    classes = [self.base_input_css_class]
    if self.css_class:
        classes.append(self.css_class)
    if self.style == styles.BOOTSTRAP_4 and self.error:
        classes.append('is-invalid')
    return ' '.join(classes)