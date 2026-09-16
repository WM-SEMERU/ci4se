def valid_kdf(self, kdf):
    if kdf.input_length is None:
        return True
    if self.data_key_length > kdf.input_length(self):
        raise InvalidAlgorithmError(
            'Invalid Algorithm definition: data_key_len must not be greater than kdf_input_len'
            )
    return True