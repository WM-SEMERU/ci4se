def match_service(service1, service2):
    s1, s2 = urlparse(service1), urlparse(service2)
    try:
        return (s1.scheme, s1.netloc, s1.path) == (s2.scheme, s2.netloc, s2
            .path)
    except ValueError:
        return False