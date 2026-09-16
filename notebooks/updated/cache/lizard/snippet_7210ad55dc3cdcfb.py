def run(interface, config, logfile, ros_args):
    logging.info(
        'pyros started with : interface {interface} config {config} logfile {logfile} ros_args {ros_args}'
        .format(interface=interface, config=config, logfile=logfile,
        ros_args=ros_args))
    if interface == 'ros':
        node_proc = pyros_rosinterface_launch(node_name=
            'pyros_rosinterface', pyros_config=config, ros_argv=ros_args)
    else:
        node_proc = None
    client_conn = node_proc.start()