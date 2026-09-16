def _get_batch(self):
    batch_data = mx.nd.zeros((self.batch_size, 3, self._data_shape[0], self
        ._data_shape[1]))
    batch_label = []
    for i in range(self.batch_size):
        if self._current + i >= self._size:
            if not self.is_train:
                continue
            idx = (self._current + i + self._size // 2) % self._size
            index = self._index[idx]
        else:
            index = self._index[self._current + i]
        im_path = self._imdb.image_path_from_index(index)
        with open(im_path, 'rb') as fp:
            img_content = fp.read()
        img = mx.img.imdecode(img_content)
        gt = self._imdb.label_from_index(index).copy(
            ) if self.is_train else None
        data, label = self._data_augmentation(img, gt)
        batch_data[i] = data
        if self.is_train:
            batch_label.append(label)
    self._data = {'data': batch_data}
    if self.is_train:
        self._label = {'label': mx.nd.array(np.array(batch_label))}
    else:
        self._label = {'label': None}