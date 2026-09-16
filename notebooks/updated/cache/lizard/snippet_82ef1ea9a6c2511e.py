def event_duration(self, obj, dictionary, low_bound=None, high_bound=None):
    data = obj.df
    N_cols = data.shape[1]
    if low_bound:
        data = data.where(data >= low_bound)
    if high_bound:
        data = data.where(data < high_bound)
    for i in range(N_cols):
        data_per_meter = data.iloc[:, ([i])]
        data_missing, meter = self.identify_missing(data_per_meter)
        uuid = self.find_uuid(obj, column_name=meter)
        data_gaps = self.diff_boolean(data_missing, meter, uuid)
        dictionary_solo = data_gaps.to_dict()
        dictionary[uuid] = dictionary_solo[uuid]
    return dictionary