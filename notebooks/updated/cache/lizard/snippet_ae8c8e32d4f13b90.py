def build_detection_dataset(folder, dataset_filename, sender_known=True):
    if os.path.exists(dataset_filename):
        os.remove(dataset_filename)
    build_detection_class(os.path.join(folder, 'P'), dataset_filename, 1)
    build_detection_class(os.path.join(folder, 'N'), dataset_filename, -1)