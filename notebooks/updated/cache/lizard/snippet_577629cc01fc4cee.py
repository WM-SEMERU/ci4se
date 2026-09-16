def convert_trees(self, ptb_trees, representation='basic', universal=True,
    include_punct=True, include_erased=False, **kwargs):
    kwargs.update(representation=representation, universal=universal,
        include_punct=include_punct, include_erased=include_erased)
    return Corpus(self.convert_tree(ptb_tree, **kwargs) for ptb_tree in
        ptb_trees)