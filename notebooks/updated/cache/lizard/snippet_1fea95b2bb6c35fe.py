def get_fields_frame(schema):
    fields = []

    def get_field_record(i, key, value, parents):
        if value.get('private') or 'default' not in value:
            raise Skip
        field = len(parents) - 1, i, tuple(parents[:-1]), parents[-1], value[
            'type'], value['default']
        return fields.append(field)
    get_types(schema['properties'], get_field_record)
    df_fields = pd.DataFrame(sorted(fields), columns=['level_i', 'field_i',
        'parents', 'field', 'field_type', 'default'])
    df_fields['attributes'] = df_fields.apply(lambda row: get_nested_item(
        row, schema['properties'], row.parents + (row.field,)), axis=1)
    return df_fields