def filter(self, iterable):
    if CSSMatch.is_tag(iterable):
        return CSSMatch(self.selectors, iterable, self.namespaces, self.flags
            ).filter()
    else:
        return [node for node in iterable if not CSSMatch.
            is_navigable_string(node) and self.match(node)]