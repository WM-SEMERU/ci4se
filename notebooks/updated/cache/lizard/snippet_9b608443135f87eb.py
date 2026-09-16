def load_image(filename, timeout=120):
    c = docker_fabric()
    with open(expand_path(filename), 'r') as f:
        _timeout = c._timeout
        c._timeout = timeout
        try:
            c.load_image(f)
        finally:
            c._timeout = _timeout