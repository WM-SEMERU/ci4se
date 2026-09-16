def rename_fields(input, **params):
    PARAM_RENAME_LIST = 'rename'
    RENAME_SRC_FIELD = 'src.field'
    RENAME_DEST_FIELD = 'dest.field'
    rename_list = params.get(PARAM_RENAME_LIST)
    for row in input:
        for rename in rename_list:
            row[rename[RENAME_DEST_FIELD]] = row[rename[RENAME_SRC_FIELD]]
            row.pop(rename[RENAME_SRC_FIELD])
    return input