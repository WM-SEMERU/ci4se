def is_active(ext, metadata):
    if metadata.get('run_control', {}).get('frozen') is True:
        return False
    if 'active' not in metadata:
        return True
    return ext.replace('.', '') in re.split('\\.|,', metadata['active'])