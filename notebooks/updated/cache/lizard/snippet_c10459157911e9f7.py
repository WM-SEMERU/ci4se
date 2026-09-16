def extract_domain(var_name, output):
    var = getenv(var_name)
    if var:
        p = urlparse(var)
        output.append(p.hostname)