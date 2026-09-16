def get_imagenet_iterator(root, batch_size, num_workers, data_shape=224,
    dtype='float32'):
    train_dir = os.path.join(root, 'train')
    train_transform, val_transform = get_imagenet_transforms(data_shape, dtype)
    logging.info('Loading image folder %s, this may take a bit long...',
        train_dir)
    train_dataset = ImageFolderDataset(train_dir, transform=train_transform)
    train_data = DataLoader(train_dataset, batch_size, shuffle=True,
        last_batch='discard', num_workers=num_workers)
    val_dir = os.path.join(root, 'val')
    if not os.path.isdir(os.path.expanduser(os.path.join(root, 'val',
        'n01440764'))):
        user_warning = (
            'Make sure validation images are stored in one subdir per category, a helper script is available at https://git.io/vNQv1'
            )
        raise ValueError(user_warning)
    logging.info('Loading image folder %s, this may take a bit long...',
        val_dir)
    val_dataset = ImageFolderDataset(val_dir, transform=val_transform)
    val_data = DataLoader(val_dataset, batch_size, last_batch='keep',
        num_workers=num_workers)
    return DataLoaderIter(train_data, dtype), DataLoaderIter(val_data, dtype)