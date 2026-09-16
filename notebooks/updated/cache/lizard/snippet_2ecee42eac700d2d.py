def get_np_dtype(nd4j_dtype):
    mapping = {'double': np.float64, 'float': np.float32, 'half': np.float16}
    np_dtype = mapping.get(nd4j_dtype)
    if not np_dtype:
        raise Exception('Invalid nd4j data type : ' + nd4j_dtype)
    return np_dtype