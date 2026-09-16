def get_provisioned_table_write_units(table_name):
    try:
        desc = DYNAMODB_CONNECTION.describe_table(table_name)
    except JSONResponseError:
        raise
    write_units = int(desc['Table']['ProvisionedThroughput'][
        'WriteCapacityUnits'])
    logger.debug('{0} - Currently provisioned write units: {1:d}'.format(
        table_name, write_units))
    return write_units