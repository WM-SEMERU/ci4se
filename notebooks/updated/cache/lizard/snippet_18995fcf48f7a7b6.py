def initializenb():
    logger.info('Working directory: {0}'.format(os.getcwd()))
    logger.info('Run on {0}'.format(asctime()))
    try:
        fileroot = os.environ['fileroot']
        logger.info('Setting fileroot to {0} from environment variable.\n'.
            format(fileroot))
        candsfile = 'cands_{0}_merge.pkl'.format(fileroot)
        noisefile = 'noise_{0}_merge.pkl'.format(fileroot)
    except KeyError:
        sdmdir = os.getcwd()
        logger.info('Setting sdmdir to current directory {0}\n'.format(os.
            path.abspath(sdmdir)))
        candsfiles = glob.glob('cands_*_merge.pkl')
        noisefiles = glob.glob('noise_*_merge.pkl')
        if len(candsfiles) == 1 and len(noisefiles) == 1:
            logger.info('Found one cands/merge file set')
        else:
            logger.warn('Found multiple cands/noise file sets. Taking first.')
        candsfile = candsfiles[0]
        noisefile = noisefiles[0]
        fileroot = candsfile.rstrip('_merge.pkl').lstrip('cands_')
    logger.info('Set: \n\t candsfile {} \n\t noisefile {} \n\t fileroot {} '
        .format(candsfile, noisefile, fileroot))
    return candsfile, noisefile, fileroot