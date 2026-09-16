def build():
    try:
        cloud_config = CloudConfig()
        config_data = cloud_config.config_data('cluster')
        cloud_init = CloudInit()
        print(cloud_init.build(config_data))
    except CloudComposeException as ex:
        print(ex)