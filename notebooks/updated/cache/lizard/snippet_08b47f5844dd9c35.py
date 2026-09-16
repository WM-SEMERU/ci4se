def get_snapshots(self):
    ec2 = self.get_ec2_connection()
    rs = ec2.get_all_snapshots()
    all_vols = [self.volume_id] + self.past_volume_ids
    snaps = []
    for snapshot in rs:
        if snapshot.volume_id in all_vols:
            if snapshot.progress == '100%':
                snapshot.date = boto.utils.parse_ts(snapshot.start_time)
                snapshot.keep = True
                snaps.append(snapshot)
    snaps.sort(cmp=lambda x, y: cmp(x.date, y.date))
    return snaps