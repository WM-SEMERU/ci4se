def get_reqs(which='main'):
    reqs = []
    for req in all_reqs[which]:
        req_str = req + '>=' + ver_tuple_to_str(min_versions[req])
        if req in version_strictly:
            req_str += ',<' + ver_tuple_to_str(min_versions[req][:-1]
                ) + '.' + str(min_versions[req][-1] + 1)
        reqs.append(req_str)
    return reqs