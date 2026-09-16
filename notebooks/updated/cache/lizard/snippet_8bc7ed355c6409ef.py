def _satisfies_conditions(self, tree_node, **kwargs):
    matches = []
    syntactic_label = kwargs.get('label', None)
    if syntactic_label:
        matches.append(bool(tree_node.labels and syntactic_label in
            tree_node.labels))
    synt_label_regexp = kwargs.get('label_regexp', None)
    if synt_label_regexp:
        if isinstance(synt_label_regexp, basestring):
            synt_label_regexp = re.compile(synt_label_regexp)
            kwargs['label_regexp'] = synt_label_regexp
        if isinstance(synt_label_regexp, RE_TYPE):
            if tree_node.labels:
                matches.append(any([(synt_label_regexp.match(label) != None
                    ) for label in tree_node.labels]))
            else:
                matches.append(False)
    word_template = kwargs.get('word_template', None)
    if word_template:
        if isinstance(word_template, WordTemplate):
            matches.append(word_template.matches(tree_node.token))
        else:
            raise Exception(
                '(!) Unexpected word_template. Should be from class WordTemplate.'
                )
    return len(matches) == 0 or all(matches)