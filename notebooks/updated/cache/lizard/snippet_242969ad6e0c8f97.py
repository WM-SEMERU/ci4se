def searchone(filename, scan, paramfile, logfile, bdfdir):
    filename = os.path.abspath(filename)
    scans = ps.read_scans(filename, bdfdir=bdfdir)
    if scan != 0:
        d = rt.set_pipeline(filename, scan, paramfile=paramfile, fileroot=
            os.path.basename(filename), logfile=logfile)
        rt.pipeline(d, range(d['nsegments']))
        pc.merge_segments(filename, scan)
        pc.merge_scans(os.path.dirname(filename), os.path.basename(filename
            ), scans.keys())
    else:
        logger.info('Scans, Target names:')
        logger.info('%s' % str([(ss, scans[ss]['source']) for ss in scans]))
        logger.info('Example pipeline:')
        state = rt.set_pipeline(filename, scans.popitem()[0], paramfile=
            paramfile, fileroot=os.path.basename(filename), logfile=logfile)