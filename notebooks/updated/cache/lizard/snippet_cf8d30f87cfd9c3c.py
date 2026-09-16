def detect_scheme(filename):
    logger = logging.getLogger(__name__)
    logger.info('Detecting partitioning scheme')
    with open(filename, 'rb') as f:
        f.seek(mbr.MBR_SIG_OFFSET)
        data = f.read(mbr.MBR_SIG_SIZE)
        signature = struct.unpack('<H', data)[0]
        if signature != mbr.MBR_SIGNATURE:
            logger.debug('Unknown partitioning scheme')
            return PartitionScheme.SCHEME_UNKNOWN
        else:
            f.seek(gpt.GPT_HEADER_OFFSET)
            data = f.read(gpt.GPT_SIG_SIZE)
            signature = struct.unpack('<8s', data)[0]
            if signature != gpt.GPT_SIGNATURE:
                logger.debug('MBR scheme detected')
                return PartitionScheme.SCHEME_MBR
            else:
                logger.debug('GPT scheme detected')
                return PartitionScheme.SCHEME_GPT