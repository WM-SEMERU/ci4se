def down(force):
    try:
        cloud_config = CloudConfig()
        cloud_controller = CloudController(cloud_config)
        cloud_controller.down(force)
    except CloudComposeException as ex:
        print(ex)