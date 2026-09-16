def std_formatter(msg):
    if isinstance(msg, dict):
        return yaml.safe_dump(msg, indent=True, default_flow_style=False)
    return str(msg)