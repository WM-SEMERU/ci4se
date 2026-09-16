def parse_dataset_key(dataset_key):
    match = re.match(DATASET_KEY_PATTERN, dataset_key)
    if not match:
        raise ValueError(
            'Invalid dataset key. Key must include user and dataset names, separated by (i.e. user/dataset).'
            )
    return match.groups()