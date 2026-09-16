def is_siemens(dicom_input):
    header = dicom_input[0]
    if 'Manufacturer' not in header or 'Modality' not in header:
        return False
    if header.Modality.upper() != 'MR':
        return False
    if 'SIEMENS' not in header.Manufacturer.upper():
        return False
    return True