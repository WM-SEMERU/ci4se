def reference_id_from_filename(filename):
    reference_id = os.path.basename(filename)
    if reference_id.rfind('.htm') > 0:
        reference_id = reference_id[:reference_id.rfind('.')]
    return reference_id