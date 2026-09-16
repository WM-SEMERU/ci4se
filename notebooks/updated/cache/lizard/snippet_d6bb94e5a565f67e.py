def _find_usage_security_groups(self):
    vpc_count = 0
    paginator = self.conn.get_paginator('describe_db_security_groups')
    for page in paginator.paginate():
        for group in page['DBSecurityGroups']:
            if 'VpcId' in group and group['VpcId'] is not None:
                vpc_count += 1
            self.limits['Max auths per security group']._add_current_usage(
                len(group['EC2SecurityGroups']) + len(group['IPRanges']),
                aws_type='AWS::RDS::DBSecurityGroup', resource_id=group[
                'DBSecurityGroupName'])
    self.limits['VPC Security Groups']._add_current_usage(vpc_count,
        aws_type='AWS::RDS::DBSecurityGroup')