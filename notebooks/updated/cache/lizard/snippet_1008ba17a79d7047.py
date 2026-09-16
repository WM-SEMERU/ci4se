def _generate_examples(self, imgs_path, csv_path):
    with tf.io.gfile.GFile(csv_path) as csv_f:
        reader = csv.DictReader(csv_f)
        label_keys = reader.fieldnames[5:]
        data = []
        for row in reader:
            name = row['Path']
            labels = [_LABELS[row[key]] for key in label_keys]
            data.append((name, labels))
    for name, labels in data:
        yield {'name': name, 'image': os.path.join(imgs_path, name),
            'label': labels}