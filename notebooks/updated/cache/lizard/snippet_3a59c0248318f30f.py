def _set_child_joined_alias(child, alias_map):
    for table in alias_map:
        join = alias_map[table]
        if not isinstance(join, Join):
            continue
        lhs = join.parent_alias
        if (lhs == child.alias and table == child.related_alias or lhs ==
            child.related_alias and table == child.alias):
            child.set_joined_alias(table)
            break