def slug(self):
    if self.is_root_node():
        return ''
    if self.slugable and self.parent.parent:
        if (not self.page.regex or self.page.regex and not self.page.
            show_regex or self.is_leaf_node()):
            return '{0}/{1}'.format(self.parent.slug, self.page.slug)
        elif self.page.regex and self.value_regex and self.page.show_regex:
            return '{0}/{1}/{2}'.format(self.parent.slug, self.page.slug,
                self.value_regex)
        elif not self.hide_in_url:
            return '{0}/{1}'.format(self.parent.slug, self.name)
    elif self.slugable:
        if (not self.page.regex or self.page.regex and not self.page.
            show_regex or self.is_leaf_node()):
            return '{0}'.format(self.page.slug)
        elif self.page.regex and self.value_regex and self.page.show_regex:
            return '{0}/{1}'.format(self.page.slug, self.value_regex)
        elif not self.hide_in_url:
            return '{0}'.format(self.name)
    return ''