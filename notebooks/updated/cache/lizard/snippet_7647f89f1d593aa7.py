def _prep_non_framed(self):
    try:
        plaintext_length = self.stream_length
        self.__unframed_plaintext_cache = self.source_stream
    except NotSupportedError:
        self.__unframed_plaintext_cache = io.BytesIO()
        self.__unframed_plaintext_cache.write(self.source_stream.read())
        plaintext_length = self.__unframed_plaintext_cache.tell()
        self.__unframed_plaintext_cache.seek(0)
    aad_content_string = (aws_encryption_sdk.internal.utils.
        get_aad_content_string(content_type=self.content_type,
        is_final_frame=True))
    associated_data = assemble_content_aad(message_id=self._header.
        message_id, aad_content_string=aad_content_string, seq_num=1,
        length=plaintext_length)
    self.encryptor = Encryptor(algorithm=self._encryption_materials.
        algorithm, key=self._derived_data_key, associated_data=
        associated_data, iv=non_framed_body_iv(self._encryption_materials.
        algorithm))
    self.output_buffer += serialize_non_framed_open(algorithm=self.
        _encryption_materials.algorithm, iv=self.encryptor.iv,
        plaintext_length=plaintext_length, signer=self.signer)