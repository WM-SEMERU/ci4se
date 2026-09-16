def set_features_types_from_dataframe(self, data_frame):
    if self.__feature_types_set:
        return
    self.__feature_types_set = True
    dtypes = data_frame.dtypes
    for feature in self.__iter__():
        name = feature.get_name()
        type_name = data_type_to_type_name(dtypes[name])
        feature.set_type_name(type_name)