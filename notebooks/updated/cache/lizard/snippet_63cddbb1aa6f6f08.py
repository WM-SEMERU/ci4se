def split(*items):
    out = []
    for data in [x[0] for x in items]:
        dis_orgs = data['config']['algorithm'].get('disambiguate')
        if dis_orgs:
            if not data.get('disambiguate', None):
                data['disambiguate'] = {'genome_build': data['genome_build'
                    ], 'base': True}
            out.append([data])
            if isinstance(dis_orgs, six.string_types):
                dis_orgs = [dis_orgs]
            for dis_org in dis_orgs:
                dis_data = copy.deepcopy(data)
                dis_data['disambiguate'] = {'genome_build': dis_org}
                dis_data['genome_build'] = dis_org
                dis_data['config']['algorithm']['effects'] = False
                dis_data = run_info.add_reference_resources(dis_data)
                out.append([dis_data])
        else:
            out.append([data])
    return out