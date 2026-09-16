def _get_value(self, scalar_data_blob, dtype_enum):
    tensorflow_dtype = tf.DType(dtype_enum)
    buf = np.frombuffer(scalar_data_blob, dtype=tensorflow_dtype.as_numpy_dtype
        )
    return np.asscalar(buf)