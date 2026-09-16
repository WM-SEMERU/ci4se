def importcalc(calc_id):
    dbserver.ensure_on()
    try:
        calc_id = int(calc_id)
    except ValueError:
        calc_id, datadir = datastore.extract_calc_id_datadir(calc_id)
        status = 'complete'
        remote = False
    else:
        remote = True
    job = logs.dbcmd('get_job', calc_id)
    if job is not None:
        sys.exit('There is already a job #%d in the local db' % calc_id)
    if remote:
        datadir = datastore.get_datadir()
        webex = WebExtractor(calc_id)
        status = webex.status['status']
        hc_id = webex.oqparam.hazard_calculation_id
        if hc_id:
            sys.exit('The job has a parent (#%d) and cannot be downloaded' %
                hc_id)
        webex.dump('%s/calc_%d.hdf5' % (datadir, calc_id))
        webex.close()
    with datastore.read(calc_id) as dstore:
        engine.expose_outputs(dstore, status=status)
    logging.info('Imported calculation %d successfully', calc_id)