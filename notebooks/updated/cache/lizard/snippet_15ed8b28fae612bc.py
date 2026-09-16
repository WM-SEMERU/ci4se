def read_calibration(detx=None, det_id=None, from_file=False, det_id_table=None
    ):
    from km3pipe.calib import Calibration
    if not (detx or det_id or from_file):
        return None
    if detx is not None:
        return Calibration(filename=detx)
    if from_file:
        det_ids = np.unique(det_id_table)
        if len(det_ids) > 1:
            log.critical('Multiple detector IDs found in events.')
        det_id = det_ids[0]
    if det_id is not None:
        if det_id < 0:
            log.warning(
                'Negative detector ID found ({0}). This is a MC detector and cannot be retrieved from the DB.'
                .format(det_id))
            return None
        return Calibration(det_id=det_id)
    return None