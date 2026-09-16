def parse_single_report(file_obj):
    parsed_data = {}
    re_groups = ['passed', 'failed', 'passed_pct', 'failed_pct']
    for k, r in flagstat_regexes.items():
        r_search = re.search(r, file_obj, re.MULTILINE)
        if r_search:
            for i, j in enumerate(re_groups):
                try:
                    key = '{}_{}'.format(k, j)
                    val = r_search.group(i + 1).strip('% ')
                    parsed_data[key] = float(val) if '.' in val else int(val)
                except IndexError:
                    pass
                except ValueError:
                    parsed_data[key] = float('nan')
    try:
        parsed_data['flagstat_total'] = parsed_data['total_passed'
            ] + parsed_data['total_failed']
    except KeyError:
        pass
    return parsed_data