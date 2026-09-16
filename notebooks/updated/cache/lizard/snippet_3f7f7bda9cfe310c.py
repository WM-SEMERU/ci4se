def _restructure_if_volume_follows_journal(left, right):

    def _get_volume_keyword_op_and_remaining_subtree(right_subtree):
        if isinstance(right_subtree, NotOp) and isinstance(right_subtree.op,
            KeywordOp) and right_subtree.op.left == Keyword('volume'):
            return None, None
        elif isinstance(right_subtree, AndOp) and isinstance(right_subtree.
            left, NotOp) and isinstance(right_subtree.left.op, KeywordOp
            ) and right_subtree.left.op.left == Keyword('volume'):
            return None, right_subtree.right
        elif isinstance(right_subtree, KeywordOp
            ) and right_subtree.left == Keyword('volume'):
            return right_subtree, None
        elif isinstance(right_subtree, AndOp
            ) and right_subtree.left.left == Keyword('volume'):
            return right_subtree.left, right_subtree.right
    journal_value = left.right.value
    volume_and_remaining_subtree = (
        _get_volume_keyword_op_and_remaining_subtree(right))
    if not volume_and_remaining_subtree:
        return
    volume_node, remaining_subtree = volume_and_remaining_subtree
    if volume_node:
        left.right.value = ','.join([journal_value, volume_node.right.value])
    return AndOp(left, remaining_subtree) if remaining_subtree else left