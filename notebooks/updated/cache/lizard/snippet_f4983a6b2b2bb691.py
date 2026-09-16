def dicom_series_to_nifti(original_dicom_directory, output_file=None,
    reorient_nifti=True):
    temp_directory = tempfile.mkdtemp()
    try:
        dicom_directory = os.path.join(temp_directory, 'dicom')
        shutil.copytree(original_dicom_directory, dicom_directory)
        dicom_input = common.read_dicom_directory(dicom_directory)
        return dicom_array_to_nifti(dicom_input, output_file, reorient_nifti)
    except AttributeError as exception:
        reraise(tp=ConversionError, value=ConversionError(str(exception)),
            tb=sys.exc_info()[2])
    finally:
        shutil.rmtree(temp_directory)