def run_config_diagnostics(config_path=CONFIG_PATH):
    config = read_config(config_path)
    missing_sections = set()
    malformed_entries = defaultdict(set)
    for section, expected_section_keys in SECTION_KEYS.items():
        section_content = config.get(section)
        if not section_content:
            missing_sections.add(section)
        else:
            for option in expected_section_keys:
                option_value = section_content.get(option)
                if not option_value:
                    malformed_entries[section].add(option)
    return config_path, missing_sections, malformed_entries