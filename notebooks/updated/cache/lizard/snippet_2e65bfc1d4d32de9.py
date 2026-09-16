def _get_sg_ids(self):
    try:
        lambda_extras = self.settings['security_groups']['lambda_extras']
    except KeyError:
        lambda_extras = []
    security_groups = [self.app_name] + lambda_extras
    sg_ids = []
    for security_group in security_groups:
        sg_id = get_security_group_id(name=security_group, env=self.env,
            region=self.region)
        sg_ids.append(sg_id)
    return sg_ids