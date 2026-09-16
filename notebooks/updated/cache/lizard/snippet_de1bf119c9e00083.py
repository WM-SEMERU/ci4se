def extract_subjects(bill):
    logger.debug('Extracting Subjects')
    subject_map = []
    subjects = bill.get('subjects', [])
    bill_id = bill.get('bill_id', None)
    bill_type = bill.get('bill_type', None)
    for sub in subjects:
        subject_map.append((bill_id, bill_type, sub))
    logger.debug('End Extractioning Subjects')
    return subject_map