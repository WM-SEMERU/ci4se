def create_blazar_client(config, session):
    return blazar_client.Client(session=session, service_type='reservation',
        region_name=os.environ['OS_REGION_NAME'])