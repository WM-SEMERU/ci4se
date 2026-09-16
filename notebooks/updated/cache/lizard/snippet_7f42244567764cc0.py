def dicom2db(file_path, file_type, is_copy, step_id, db_conn,
    sid_by_patient=False, pid_in_vid=False, visit_in_path=False,
    rep_in_path=False):
    global conn
    conn = db_conn
    tags = dict()
    logging.info("Extracting DICOM headers from '%s'" % file_path)
    try:
        dcm = dicom.read_file(file_path)
        dataset = db_conn.get_dataset(step_id)
        tags['participant_id'] = _extract_participant(dcm, dataset, pid_in_vid)
        if visit_in_path:
            tags['visit_id'] = _extract_visit_from_path(dcm, file_path,
                pid_in_vid, sid_by_patient, dataset, tags['participant_id'])
        else:
            tags['visit_id'] = _extract_visit(dcm, dataset, tags[
                'participant_id'], sid_by_patient, pid_in_vid)
        tags['session_id'] = _extract_session(dcm, tags['visit_id'])
        tags['sequence_type_id'] = _extract_sequence_type(dcm)
        tags['sequence_id'] = _extract_sequence(tags['session_id'], tags[
            'sequence_type_id'])
        if rep_in_path:
            tags['repetition_id'] = _extract_repetition_from_path(dcm,
                file_path, tags['sequence_id'])
        else:
            tags['repetition_id'] = _extract_repetition(dcm, tags[
                'sequence_id'])
        tags['file_id'] = extract_dicom(file_path, file_type, is_copy, tags
            ['repetition_id'], step_id)
    except InvalidDicomError:
        logging.warning('%s is not a DICOM file !' % step_id)
    except IntegrityError:
        logging.warning(
            'A problem occurred with the DB ! A rollback will be performed...')
        conn.db_session.rollback()
    return tags