def _find_usage_instances(self):
    paginator = self.conn.get_paginator('describe_db_instances')
    for page in paginator.paginate():
        for instance in page['DBInstances']:
            self.limits['Read replicas per master']._add_current_usage(len(
                instance['ReadReplicaDBInstanceIdentifiers']), aws_type=
                'AWS::RDS::DBInstance', resource_id=instance[
                'DBInstanceIdentifier'])