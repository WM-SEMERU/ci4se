def map_across_blocks(self, map_func):
    preprocessed_map_func = self.preprocess_func(map_func)
    new_partitions = np.array([[part.apply(preprocessed_map_func) for part in
        row_of_parts] for row_of_parts in self.partitions])
    return self.__constructor__(new_partitions)