def to_code(self, context: Context=None):
    context = context or Context()
    for imp in self.imports:
        if imp not in context.imports:
            context.imports.append(imp)
    counter = Counter()
    lines = list(self.to_lines(context=context, counter=counter))
    if counter.num_indented_non_doc_blocks == 0:
        if self.expects_body_or_pass:
            lines.append('    pass')
        elif self.closed_by:
            lines[-1] += self.closed_by
    elif self.closed_by:
        lines.append(self.closed_by)
    return join_lines(*lines) + self._suffix