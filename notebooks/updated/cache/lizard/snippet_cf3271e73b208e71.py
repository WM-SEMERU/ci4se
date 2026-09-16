def add_sqlvm_to_group(instance, sql_virtual_machine_group_resource_id,
    sql_service_account_password, cluster_operator_account_password,
    cluster_bootstrap_account_password=None):
    if not is_valid_resource_id(sql_virtual_machine_group_resource_id):
        raise CLIError('Invalid SQL virtual machine group resource id.')
    instance.sql_virtual_machine_group_resource_id = (
        sql_virtual_machine_group_resource_id)
    instance.wsfc_domain_credentials = WsfcDomainCredentials(
        cluster_bootstrap_account_password=
        cluster_bootstrap_account_password,
        cluster_operator_account_password=cluster_operator_account_password,
        sql_service_account_password=sql_service_account_password)
    return instance