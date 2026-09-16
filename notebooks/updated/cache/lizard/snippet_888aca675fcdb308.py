def __get_min_reads(current_provisioning, min_provisioned_reads, log_tag):
    reads = 1
    if min_provisioned_reads:
        reads = int(min_provisioned_reads)
        if reads > int(current_provisioning * 2):
            reads = int(current_provisioning * 2)
            logger.debug(
                '{0} - Cannot reach min-provisioned-reads as max scale up is 100% of current provisioning'
                .format(log_tag))
    logger.debug('{0} - Setting min provisioned reads to {1}'.format(
        log_tag, min_provisioned_reads))
    return reads