def create_vpc_flow_logs(self, account, region, vpc_id, iam_role_arn):
    try:
        flow = self.session.client('ec2', region)
        flow.create_flow_logs(ResourceIds=[vpc_id], ResourceType='VPC',
            TrafficType='ALL', LogGroupName=vpc_id,
            DeliverLogsPermissionArn=iam_role_arn)
        fvpc = VPC.get(vpc_id)
        fvpc.set_property('vpc_flow_logs_status', 'ACTIVE')
        self.log.info('Enabled VPC Logging {}/{}/{}'.format(account, region,
            vpc_id))
        auditlog(event='vpc_flow_logs.create_vpc_flow', actor=self.ns, data
            ={'account': account.account_name, 'region': region, 'vpcId':
            vpc_id, 'arn': iam_role_arn})
    except Exception:
        self.log.exception('Failed creating VPC Flow Logs for {}/{}/{}.'.
            format(account, region, vpc_id))