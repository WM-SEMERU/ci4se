def add_policy(self, scaling_group, name, policy_type, cooldown, change=
    None, is_percent=False, desired_capacity=None, args=None):
    uri = '/%s/%s/policies' % (self.uri_base, utils.get_id(scaling_group))
    body = self._create_policy_body(name, policy_type, cooldown, change=
        change, is_percent=is_percent, desired_capacity=desired_capacity,
        args=args)
    body = [body]
    resp, resp_body = self.api.method_post(uri, body=body)
    pol_info = resp_body.get('policies')[0]
    return AutoScalePolicy(self, pol_info, scaling_group)