def _set_child_joined_alias_using_join_map(child, join_map, alias_map):
    for lhs, table, join_cols in join_map:
        if lhs is None:
            continue
        if lhs == child.alias:
            relevant_alias = child.related_alias
        elif lhs == child.related_alias:
            relevant_alias = child.alias
        else:
            continue
        join_info = alias_map[relevant_alias]
        if join_info.join_type is None:
            continue
        if join_info.lhs_alias in [child.alias, child.related_alias]:
            child.set_joined_alias(relevant_alias)
            break