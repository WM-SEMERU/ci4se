def data_response(self):
    d = []
    for i in range(self._num_bands):
        if self._compute_bool[i] is True:
            d_i = self._imageModel_list[i].data_response
            if d == []:
                d = d_i
            else:
                d = np.append(d, d_i)
    return d