def transform(data, target_wd, target_ht, is_train, box):
    if box is not None:
        x, y, w, h = box
        data = data[y:min(y + h, data.shape[0]), x:min(x + w, data.shape[1])]
    data = mx.image.imresize(data, target_wd, target_ht)
    data = data.astype(np.float32) / 255.0
    data = (data - mx.nd.array([0.485, 0.456, 0.406])) / mx.nd.array([0.229,
        0.224, 0.225])
    if is_train:
        if random.random() < 0.5:
            data = nd.flip(data, axis=1)
        data, _ = mx.image.random_crop(data, (224, 224))
    else:
        data, _ = mx.image.center_crop(data, (224, 224))
    data = nd.transpose(data, (2, 0, 1))
    if data.shape[0] == 1:
        data = nd.tile(data, (3, 1, 1))
    return data.reshape((1,) + data.shape)