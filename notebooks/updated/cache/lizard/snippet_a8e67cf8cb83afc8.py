def _remove_single_line_import_comments(r):
    logging.info('Removing single line import comments')
    import_r, remaining_r = split_by_last_import(r)
    new_import_r = redbaron.NodeList()
    for i, v in enumerate(import_r):
        if 1 < i < len(import_r) - 2:
            if not (import_r[i - 2].type != 'comment' and v.type ==
                'comment' and import_r[i + 2].type != 'comment'
                ) or _is_keep_comment(v):
                new_import_r.append(v)
        else:
            new_import_r.append(v)
    return new_import_r + remaining_r