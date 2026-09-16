def sync_one(self, aws_syncr, amazon, role):
    trust_document = role.trust.document
    attached_policies = role.attached_policies
    permission_document = role.permission.document
    policy_name = 'syncr_policy_{0}'.format(role.name.replace('/', '__'))
    role_info = amazon.iam.role_info(role.name)
    if not role_info:
        amazon.iam.create_role(role.name, trust_document, policies={
            policy_name: permission_document}, attached_policies=
            attached_policies)
    else:
        amazon.iam.modify_role(role_info, role.name, trust_document,
            policies={policy_name: permission_document}, attached_policies=
            attached_policies)
    if role.make_instance_profile:
        amazon.iam.make_instance_profile(role.name)