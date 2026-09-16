def parse_repeating_time_interval_to_str(date_str):
    with open(os.path.join(ABSOLUTE_SCHEMA_DIR, 'accrualPeriodicity.json'), 'r'
        ) as f:
        freqs_map = {freq['id']: freq['description'] for freq in json.load(f)}
    return freqs_map[date_str]