def compress_message(data_to_compress):
    compressed_content = cms.ParsableOctetString(zlib.compress(
        data_to_compress))
    return cms.ContentInfo({'content_type': cms.ContentType(
        'compressed_data'), 'content': cms.CompressedData({'version': cms.
        CMSVersion('v0'), 'compression_algorithm': cms.CompressionAlgorithm
        ({'algorithm': cms.CompressionAlgorithmId('zlib')}),
        'encap_content_info': cms.EncapsulatedContentInfo({'content_type':
        cms.ContentType('data'), 'content': compressed_content})})}).dump()