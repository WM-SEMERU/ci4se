def generate_models(args):
    data_table = get_data_table(args.filename)
    tables = to_tables(data_table.rows_to_dicts())
    attr_indent = '\n' + args.indent * 2
    attr_sep = ',' + attr_indent
    for tname, cols in tables.items():
        model_name = table_to_model_name(tname, list(cols.values())[0][
            'table_schema'])
        pk_cols, oth_cols = split_pks(cols)
        timestamps = get_timestamps(cols, args.created_at_col_name, args.
            updated_at_col_name)
        is_auto = len(pk_cols) == 1 and cols[pk_cols[0]]['is_auto'] == 't'
        attrs = OrderedDict()
        for cname in oth_cols:
            if cname not in timestamps:
                attrs[cname] = None
        print(_MODEL_SOURCE.format(class_name=model_name, base_class_name=
            'ModelBase', indent=args.indent, table_name=repr(tname),
            pk_name=repr(pk_cols[0] if len(pk_cols) == 1 else pk_cols),
            pk_is_auto=is_auto, timestamps=timestamps, attrs='dict(' +
            attr_indent + attr_sep.join('{0}={1}'.format(k, v) for k, v in
            attrs.items()) + ')'))
        print()