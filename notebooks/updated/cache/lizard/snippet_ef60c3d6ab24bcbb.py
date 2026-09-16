def _filter_db_instances_by_status(awsclient, db_instances, status_list):
    client_rds = awsclient.get_client('rds')
    db_instances_with_status = []
    for db in db_instances:
        response = client_rds.describe_db_instances(DBInstanceIdentifier=db)
        for entry in response.get('DBInstances', []):
            if entry['DBInstanceStatus'] in status_list:
                db_instances_with_status.append(db)
    return db_instances_with_status