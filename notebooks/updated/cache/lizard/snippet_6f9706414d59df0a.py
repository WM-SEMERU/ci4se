def _get_first_header(dicom_directory):
    for root, _, file_names in os.walk(dicom_directory):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            if not compressed_dicom.is_dicom_file(file_path):
                continue
            return compressed_dicom.read_file(file_path, stop_before_pixels
                =True, force=dicom2nifti.settings.pydicom_read_force)
    raise ConversionError('NO_DICOM_FILES_FOUND')