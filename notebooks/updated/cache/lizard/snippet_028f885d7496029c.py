def checksum(thing):
    try:
        job_id = int(thing)
        job_file = None
    except ValueError:
        job_id = None
        job_file = thing
        if not os.path.exists(job_file):
            sys.exit('%s does not correspond to an existing file' % job_file)
    if job_id:
        dstore = util.read(job_id)
        checksum = dstore['/'].attrs['checksum32']
    elif job_file.endswith('.xml'):
        inputs = {'source_model_logic_tree': job_file}
        checksum = readinput.get_checksum32(mock.Mock(inputs=inputs))
    else:
        oq = readinput.get_oqparam(job_file)
        checksum = readinput.get_checksum32(oq)
    print(checksum)