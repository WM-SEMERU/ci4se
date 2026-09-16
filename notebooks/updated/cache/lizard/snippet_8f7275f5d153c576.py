def shuffle_records(fname):
    tf.logging.info('Shuffling records in file %s' % fname)
    tmp_fname = fname + '.unshuffled'
    tf.gfile.Rename(fname, tmp_fname)
    reader = tf.python_io.tf_record_iterator(tmp_fname)
    records = []
    for record in reader:
        records.append(record)
        if len(records) % 100000 == 0:
            tf.logging.info('\tRead: %d', len(records))
    random.shuffle(records)
    with tf.python_io.TFRecordWriter(fname) as w:
        for count, record in enumerate(records):
            w.write(record)
            if count > 0 and count % 100000 == 0:
                tf.logging.info('\tWriting record: %d' % count)
    tf.gfile.Remove(tmp_fname)