def check_platforms(platforms):
    if len(platforms) > 0:
        return all(platform in PLATFORM_IDS for platform in platforms)
    return True