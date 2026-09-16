def variable_length_to_fixed_length_categorical(self, left_edge=4,
    right_edge=4, max_length=15):
    cache_key = 'fixed_length_categorical', left_edge, right_edge, max_length
    if cache_key not in self.encoding_cache:
        fixed_length_sequences = (self.
            sequences_to_fixed_length_index_encoded_array(self.sequences,
            left_edge=left_edge, right_edge=right_edge, max_length=max_length))
        self.encoding_cache[cache_key] = fixed_length_sequences
    return self.encoding_cache[cache_key]