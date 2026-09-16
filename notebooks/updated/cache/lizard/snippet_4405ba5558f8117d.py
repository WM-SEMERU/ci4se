def _parse_or_match(self, text, pos, method_name):
    if not self.grammar:
        raise RuntimeError(
            "The {cls}.{method}() shortcut won't work because {cls} was never associated with a specific grammar. Fill out its `grammar` attribute, and try again."
            .format(cls=self.__class__.__name__, method=method_name))
    return self.visit(getattr(self.grammar, method_name)(text, pos=pos))