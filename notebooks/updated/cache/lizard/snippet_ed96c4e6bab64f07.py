def prepare(self, data_source):
    dataframe = self.__get_dataframe(data_source, use_target=True)
    self.__config.get_data_model().set_features_types_from_dataframe(dataframe)
    dataframe = self.__cleaner.prepare(dataframe)
    return self.__transformer.prepare(dataframe)