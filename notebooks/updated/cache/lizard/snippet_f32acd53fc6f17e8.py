def get_all_dbsecurity_groups(self, groupname=None, max_records=None,
    marker=None):
    params = {}
    if groupname:
        params['DBSecurityGroupName'] = groupname
    if max_records:
        params['MaxRecords'] = max_records
    if marker:
        params['Marker'] = marker
    return self.get_list('DescribeDBSecurityGroups', params, [(
        'DBSecurityGroup', DBSecurityGroup)])