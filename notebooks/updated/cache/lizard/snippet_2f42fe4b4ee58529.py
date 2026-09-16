def __get_connection_SNS():
    region = get_global_option('region')
    try:
        if get_global_option('aws_access_key_id') and get_global_option(
            'aws_secret_access_key'):
            logger.debug(
                'Authenticating to SNS using credentials in configuration file'
                )
            connection = sns.connect_to_region(region, aws_access_key_id=
                get_global_option('aws_access_key_id'),
                aws_secret_access_key=get_global_option(
                'aws_secret_access_key'))
        else:
            logger.debug("Authenticating using boto's authentication handler")
            connection = sns.connect_to_region(region)
    except Exception as err:
        logger.error('Failed connecting to SNS: {0}'.format(err))
        logger.error(
            'Please report an issue at: https://github.com/sebdah/dynamic-dynamodb/issues'
            )
        raise
    logger.debug('Connected to SNS in {0}'.format(region))
    return connection