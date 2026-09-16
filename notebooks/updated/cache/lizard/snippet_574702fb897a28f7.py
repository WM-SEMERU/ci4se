def _find_usage_ACLs(self):
    acls = defaultdict(int)
    for acl in self.conn.describe_network_acls()['NetworkAcls']:
        acls[acl['VpcId']] += 1
        self.limits['Rules per network ACL']._add_current_usage(len(acl[
            'Entries']), aws_type='AWS::EC2::NetworkAcl', resource_id=acl[
            'NetworkAclId'])
    for vpc_id in acls:
        self.limits['Network ACLs per VPC']._add_current_usage(acls[vpc_id],
            aws_type='AWS::EC2::VPC', resource_id=vpc_id)