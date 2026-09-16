def write_config(config_data: Dict[str, Path], path: Path=None):
    path = Path(path) if path else infer_config_base_dir()
    valid_names = [ce.name for ce in CONFIG_ELEMENTS]
    try:
        os.makedirs(path, exist_ok=True)
        with (path / _CONFIG_FILENAME).open('w') as base_f:
            json.dump({k: str(v) for k, v in config_data.items() if k in
                valid_names}, base_f, indent=2)
    except OSError as e:
        sys.stderr.write('Config index write to {} failed: {}\n'.format(
            path / _CONFIG_FILENAME, e))