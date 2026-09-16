def _get_fold_levels(editor):
    block = editor.document().firstBlock()
    oed = editor.get_outlineexplorer_data()
    folds = []
    parents = []
    prev = None
    while block.isValid():
        if TextBlockHelper.is_fold_trigger(block):
            try:
                data = oed[block.firstLineNumber()]
                if data.def_type in (OED.CLASS, OED.FUNCTION):
                    fsh = FoldScopeHelper(FoldScope(block), data)
                    _adjust_parent_stack(fsh, prev, parents)
                    fsh.parents = copy.copy(parents)
                    folds.append(fsh)
                    prev = fsh
            except KeyError:
                pass
        block = block.next()
    return folds