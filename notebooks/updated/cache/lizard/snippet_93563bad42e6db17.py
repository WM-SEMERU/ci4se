def get_provisioned_gsi_write_units(table_name, gsi_name):
    try:
        desc = DYNAMODB_CONNECTION.describe_table(table_name)
    except JSONResponseError:
        raise
    for gsi in desc['Table']['GlobalSecondaryIndexes']:
        if gsi['IndexName'] == gsi_name:
            write_units = int(gsi['ProvisionedThroughput'][
                'WriteCapacityUnits'])
            break
    logger.debug('{0} - GSI: {1} - Currently provisioned write units: {2:d}'
        .format(table_name, gsi_name, write_units))
    return write_units