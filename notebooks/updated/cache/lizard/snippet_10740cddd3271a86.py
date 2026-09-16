def get_pattern(self):
    if self.is_root_node():
        return ''
    else:
        parent_pattern = self.parent.get_pattern()
        if parent_pattern != '':
            parent_pattern = '{}'.format(parent_pattern)
        if not self.page and not self.is_leaf_node():
            if self.hide_in_url:
                return '{0}'.format(parent_pattern)
            else:
                return '{0}{1}'.format(parent_pattern, self.name)
        elif self.is_leaf_node() and self.page.regex and self.page.show_regex:
            return '{0}{1}/{2}'.format(parent_pattern, self.page.slug, self
                .page.regex)
        elif self.is_leaf_node() and (not self.page.regex or not self.page.
            show_regex):
            return '{0}{1}/'.format(parent_pattern, self.page.slug)
        elif not self.is_leaf_node(
            ) and self.page.regex and self.page.show_regex:
            return '{0}{1}/{2}/'.format(parent_pattern, self.page.slug,
                self.page.regex)
        else:
            return '{0}{1}/'.format(parent_pattern, self.page.slug)