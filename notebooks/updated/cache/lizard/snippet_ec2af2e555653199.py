def nagios(self, stream=sys.stdout):
    warnings = []
    criticals = []
    for class_name, job_class in self.config.crontabber.jobs.class_list:
        if job_class.app_name in self.job_state_database:
            info = self.job_state_database.get(job_class.app_name)
            if not info.get('error_count', 0):
                continue
            error_count = info['error_count']
            serialized = '%s (%s) | %s | %s' % (job_class.app_name,
                class_name, info['last_error']['type'], info['last_error'][
                'value'])
            if error_count == 1 and hasattr(job_class, '_is_backfill_app'):
                warnings.append(serialized)
            else:
                criticals.append(serialized)
    if criticals:
        stream.write('CRITICAL - ')
        stream.write('; '.join(criticals))
        stream.write('\n')
        return 2
    elif warnings:
        stream.write('WARNING - ')
        stream.write('; '.join(warnings))
        stream.write('\n')
        return 1
    stream.write('OK - All systems nominal')
    stream.write('\n')
    return 0