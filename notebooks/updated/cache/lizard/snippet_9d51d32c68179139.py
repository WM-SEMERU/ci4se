def get_inst_info(qry_string):
    qry_prefix = 'EC2C.describe_instances('
    qry_real = qry_prefix + qry_string + ')'
    qry_results = eval(qry_real)
    return qry_results