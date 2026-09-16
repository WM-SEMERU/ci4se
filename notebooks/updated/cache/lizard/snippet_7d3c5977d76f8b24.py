def create_channel(api_key, api_secret, channel_type='manual', **kwargs):
    jwplatform_client = jwplatform.Client(api_key, api_secret)
    logging.info('Creating new channel with keyword args.')
    try:
        response = jwplatform_client.channels.create(type=channel_type, **
            kwargs)
    except jwplatform.errors.JWPlatformError as e:
        logging.error('Encountered an error creating new channel.\n{}'.
            format(e))
        sys.exit(e.message)
    return response