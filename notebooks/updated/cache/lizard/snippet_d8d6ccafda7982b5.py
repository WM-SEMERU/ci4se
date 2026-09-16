def increase_reads_in_percent(current_provisioning, percent,
    max_provisioned_reads, consumed_read_units_percent, log_tag):
    current_provisioning = float(current_provisioning)
    consumed_read_units_percent = float(consumed_read_units_percent)
    percent = float(percent)
    consumption_based_current_provisioning = float(math.ceil(
        current_provisioning * (consumed_read_units_percent / 100)))
    if consumption_based_current_provisioning > current_provisioning:
        increase = int(math.ceil(consumption_based_current_provisioning * (
            percent / 100)))
        updated_provisioning = (consumption_based_current_provisioning +
            increase)
    else:
        increase = int(math.ceil(current_provisioning * (percent / 100)))
        updated_provisioning = current_provisioning + increase
    if max_provisioned_reads > 0:
        if updated_provisioning > max_provisioned_reads:
            logger.info('{0} - Reached provisioned reads max limit: {1}'.
                format(log_tag, max_provisioned_reads))
            return max_provisioned_reads
    logger.debug('{0} - Read provisioning will be increased to {1} units'.
        format(log_tag, updated_provisioning))
    return updated_provisioning