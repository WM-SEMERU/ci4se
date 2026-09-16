def to_gremlin(self):
    self.validate()
    template = 'copySplit({recurse}).exhaustMerge'
    recurse_base = '_()'
    recurse_traversal = ".{direction}('{edge_name}')".format(direction=self
        .direction, edge_name=self.edge_name)
    recurse_steps = [(recurse_base + recurse_traversal * i) for i in six.
        moves.xrange(self.depth + 1)]
    recursion_string = template.format(recurse=','.join(recurse_steps))
    if self.within_optional_scope:
        recurse_template = (
            'ifThenElse{{it == null}}{{null}}{{it.{recursion_string}}}')
        return recurse_template.format(recursion_string=recursion_string)
    else:
        return recursion_string