def lower_comparisons_to_between(match_query):
    new_match_traversals = []
    for current_match_traversal in match_query.match_traversals:
        new_traversal = []
        for step in current_match_traversal:
            if step.where_block:
                expression = step.where_block.predicate
                new_where_block = Filter(_lower_expressions_to_between(
                    expression))
                new_traversal.append(step._replace(where_block=new_where_block)
                    )
            else:
                new_traversal.append(step)
        new_match_traversals.append(new_traversal)
    return match_query._replace(match_traversals=new_match_traversals)