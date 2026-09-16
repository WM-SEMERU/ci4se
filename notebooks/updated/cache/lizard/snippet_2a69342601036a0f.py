def is_higher_permission(level1, level2):
    return is_publish_permission(level1) and not is_publish_permission(level2
        ) or is_edit_permission(level1) and not is_publish_permission(level2
        ) and not is_edit_permission(level2) or is_showon_permission(level1
        ) and is_view_permission(level2)