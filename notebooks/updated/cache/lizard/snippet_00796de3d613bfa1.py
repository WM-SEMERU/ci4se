def get_os_dist_info():
    distribution = platform.dist()
    dist_name = distribution[0].lower()
    dist_version_str = distribution[1]
    if dist_name and dist_version_str:
        return dist_name, dist_version_str
    else:
        return None, None