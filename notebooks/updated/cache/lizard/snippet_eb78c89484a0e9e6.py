def to_html(self):
    icon = self.html_icon()
    attributes = self.html_attributes()
    wrappable_text = self.to_text().replace(os.sep, '<wbr>' + os.sep)
    if icon is not '' and attributes is not '':
        return '<span%s>%s%s</span>' % (attributes, icon, wrappable_text)
    else:
        return self.to_text()