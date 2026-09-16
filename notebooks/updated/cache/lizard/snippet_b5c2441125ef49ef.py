def _convert_asset_timestamp_fields(dict_):
    for key in (_asset_timestamp_fields & viewkeys(dict_)):
        value = pd.Timestamp(dict_[key], tz='UTC')
        dict_[key] = None if isnull(value) else value
    return dict_