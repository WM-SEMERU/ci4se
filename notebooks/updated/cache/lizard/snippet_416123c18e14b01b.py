def handle_flagged_args(args, config):
    error = None
    os_version = str()
    os_type = str()
    os_category = BuildError(args, msg='Invalid build config', frame=gfi(cf()))
    for item in expected_operations:
        if item.name == args['os_type']:
            for version in item.versions:
                os_version = version
                os_type = item.os_type
                if item.os_category == 'redhat':
                    os_category = build_redhat
                elif item.os_category == 'debian':
                    os_category = build_debian
                else:
                    error = False
                    os_category = os_category.print_msg
                break
    error = os_category(config, os_version, os_type=os_type
        ) if error else error