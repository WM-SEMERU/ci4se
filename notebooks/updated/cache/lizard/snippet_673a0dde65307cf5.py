def retrieve(run_id, det_id, outfile=None):
    try:
        det_id = int(det_id)
    except ValueError:
        pass
    path = irods_filepath(det_id, run_id)
    suffix = '' if outfile is None else outfile
    os.system('iget -Pv {0} {1}'.format(path, suffix))