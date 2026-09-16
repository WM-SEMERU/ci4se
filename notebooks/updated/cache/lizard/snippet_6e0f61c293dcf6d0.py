def create_checksum_object_from_bytes(b, algorithm=d1_common.const.
    DEFAULT_CHECKSUM_ALGORITHM):
    checksum_str = calculate_checksum_on_bytes(b, algorithm)
    checksum_pyxb = d1_common.types.dataoneTypes.checksum(checksum_str)
    checksum_pyxb.algorithm = algorithm
    return checksum_pyxb