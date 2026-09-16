def EncodeMessageList(cls, message_list, packed_message_list):
    uncompressed_data = message_list.SerializeToString()
    packed_message_list.message_list = uncompressed_data
    compressed_data = zlib.compress(uncompressed_data)
    if len(compressed_data) < len(uncompressed_data):
        packed_message_list.compression = (rdf_flows.PackedMessageList.
            CompressionType.ZCOMPRESSION)
        packed_message_list.message_list = compressed_data