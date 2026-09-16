def convert_nested_to_dataframe(agg, dates_as_key=True):
    crossed_cats_expanded = []
    high_level_returning = False
    agg_as_dict = agg.to_dict()
    cat_names = [item for item in agg_as_dict.keys() if type(agg_as_dict[
        item]) is dict]
    for cat_name in cat_names:
        expanded_buckets = []
        merge_vert = False
        if not len(getattr(agg, cat_name).buckets):
            raise ValueError(
                'There is no count data in the lowest level of nesting. Is your search setup correctly?'
                )
        for bucket in getattr(agg, cat_name).buckets:
            bucket_as_dict = bucket.to_dict()
            if dict not in [type(item) for item in bucket_as_dict.values()]:
                if 'key_as_string' in bucket_as_dict.keys() and dates_as_key:
                    bucket_as_dict['key'] = bucket['key_as_string']
                    bucket_as_dict.pop('key_as_string')
                bucket_as_dict[cat_name] = bucket_as_dict.pop('key')
                expanded_buckets.append(bucket_as_dict)
            else:
                level_name = str(bucket.key)
                lower_level_return = convert_nested_to_dataframe(bucket)
                expanded_buckets.append(add_category_labels(level_name,
                    cat_name, lower_level_return))
                merge_vert = True
        if not merge_vert:
            dataframe_out = pd.DataFrame(expanded_buckets)
            dataframe_out.rename(columns=lambda x: x.replace('key', cat_name))
            crossed_cats_expanded.append(dataframe_out.reset_index(drop=True))
            high_level_returning = True
    if high_level_returning:
        return pd.concat(crossed_cats_expanded, axis=1).reset_index(drop=True)
    else:
        return pd.concat(expanded_buckets, axis=0).reset_index(drop=True)