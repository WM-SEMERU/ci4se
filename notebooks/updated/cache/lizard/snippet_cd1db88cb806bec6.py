def ip_ignore(self, project):
    project_list = False
    try:
        ip_ignore = il['ip_ignore']
    except KeyError:
        logger.error('Key Error processing ip_ignore list values')
    try:
        project_exceptions = il.get('project_exceptions')
        for item in project_exceptions:
            if project in item:
                exception_file = item.get(project)
                with open(exception_file, 'r') as f:
                    ip_list = yaml.safe_load(f)
                    project_list = ip_list['ip_ignore']
    except KeyError:
        logger.info('No ip_ignore for %s', project)
    if project_list:
        ip_ignore = ip_ignore + project_list
        ip_ignore_re = re.compile('|'.join(ip_ignore), flags=re.IGNORECASE)
        return ip_ignore_re
    else:
        ip_ignore_re = re.compile('|'.join(ip_ignore), flags=re.IGNORECASE)
        return ip_ignore_re