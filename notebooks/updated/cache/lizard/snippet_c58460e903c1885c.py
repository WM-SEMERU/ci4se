def check_requirements_file(req_file, skip_packages):
    reqs = read_requirements(req_file)
    if skip_packages is not None:
        reqs = [req for req in reqs if req.name not in skip_packages]
    outdated_reqs = filter(None, [check_req(req) for req in reqs])
    return outdated_reqs