def _get_columns_relevant_for_diff(columns_to_show):
    cols = set([col.title for col in columns_to_show if col.relevant_for_diff])
    if len(cols) == 0:
        return set([col.title for col in columns_to_show if col.title ==
            'status'])
    else:
        return cols