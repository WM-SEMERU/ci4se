def _find_usage_snapshots(self):
    logger.debug('Getting usage for EBS snapshots')
    snaps = paginate_dict(self.conn.describe_snapshots, OwnerIds=['self'],
        alc_marker_path=['NextToken'], alc_data_path=['Snapshots'],
        alc_marker_param='NextToken')
    self.limits['Active snapshots']._add_current_usage(len(snaps[
        'Snapshots']), aws_type='AWS::EC2::VolumeSnapshot')