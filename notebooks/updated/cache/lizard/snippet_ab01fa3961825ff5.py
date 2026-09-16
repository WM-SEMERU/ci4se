def scan_file(path):
    path = os.path.abspath(path)
    if settings.USE_CLAMD:
        return clamd.scan_file(path)
    else:
        return clamscan.scan_file(path)