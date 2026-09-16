def _update_usage_for_nlb(self, conn, nlb_arn, nlb_name):
    logger.debug('Updating usage for NLB %s', nlb_arn)
    listeners = paginate_dict(conn.describe_listeners, LoadBalancerArn=
        nlb_arn, alc_marker_path=['NextMarker'], alc_data_path=['Listeners'
        ], alc_marker_param='Marker')['Listeners']
    self.limits['Listeners per network load balancer']._add_current_usage(len
        (listeners), aws_type=
        'AWS::ElasticLoadBalancingV2::NetworkLoadBalancer', resource_id=
        nlb_name)