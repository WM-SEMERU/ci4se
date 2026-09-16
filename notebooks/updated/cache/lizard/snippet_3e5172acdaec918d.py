def capture(board):
    game = Game()
    v = 0, 0
    stub_actor = base.Actor('capture', v, v, v, v, v, v, v, v, v)
    root = base.State(board, stub_actor, stub_actor, turn=1,
        actions_remaining=1)
    solution_node = None
    for eot in game.all_ends_of_turn(root):
        if eot.is_mana_drain:
            if eot.parent.board.is_empty():
                solution_node = eot
                break
    solution_sequence = list()
    if solution_node:
        node = solution_node
        while node:
            if not isinstance(node, base.Swap):
                node = node.parent
                continue
            summary = base.Summary(node.parent.board, node.position_pair,
                None, None, None)
            solution_sequence.append(summary)
            node = node.parent
    return tuple(reversed(solution_sequence))