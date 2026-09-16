def dicom_array_to_nifti(dicom_list, output_file, reorient_nifti=True):
    if not are_imaging_dicoms(dicom_list):
        raise ConversionValidationError('NON_IMAGING_DICOM_FILES')
    vendor = _get_vendor(dicom_list)
    if vendor == Vendor.GENERIC:
        results = convert_generic.dicom_to_nifti(dicom_list, output_file)
    elif vendor == Vendor.SIEMENS:
        results = convert_siemens.dicom_to_nifti(dicom_list, output_file)
    elif vendor == Vendor.GE:
        results = convert_ge.dicom_to_nifti(dicom_list, output_file)
    elif vendor == Vendor.PHILIPS:
        results = convert_philips.dicom_to_nifti(dicom_list, output_file)
    elif vendor == Vendor.HITACHI:
        results = convert_hitachi.dicom_to_nifti(dicom_list, output_file)
    else:
        raise ConversionValidationError('UNSUPPORTED_DATA')
    if reorient_nifti or settings.resample:
        image_reorientation.reorient_image(results['NII_FILE'], results[
            'NII_FILE'])
    if settings.resample:
        if not common.is_orthogonal_nifti(results['NII_FILE']):
            resample.resample_single_nifti(results['NII_FILE'])
    return results