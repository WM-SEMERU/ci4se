def __update_throughput(table_name, key_name, read_units, write_units):
    try:
        current_ru = dynamodb.get_provisioned_table_read_units(table_name)
        current_wu = dynamodb.get_provisioned_table_write_units(table_name)
    except JSONResponseError:
        raise
    try:
        table_status = dynamodb.get_table_status(table_name)
    except JSONResponseError:
        raise
    logger.debug('{0} - Table status is {1}'.format(table_name, table_status))
    if table_status != 'ACTIVE':
        logger.warning(
            '{0} - Not performing throughput changes when table is {1}'.
            format(table_name, table_status))
        return
    if get_table_option(key_name, 'always_decrease_rw_together'):
        read_units, write_units = __calculate_always_decrease_rw_values(
            table_name, read_units, current_ru, write_units, current_wu)
        if read_units == current_ru and write_units == current_wu:
            logger.info('{0} - No changes to perform'.format(table_name))
            return
    dynamodb.update_table_provisioning(table_name, key_name, int(read_units
        ), int(write_units))