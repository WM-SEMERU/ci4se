def _position_encoding_init(max_length, dim):
    position_enc = np.arange(max_length).reshape((-1, 1)) / np.power(10000,
        2.0 / dim * np.arange(dim).reshape((1, -1)))
    position_enc[:, 0::2] = np.sin(position_enc[:, 0::2])
    position_enc[:, 1::2] = np.cos(position_enc[:, 1::2])
    return position_enc