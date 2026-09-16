def _get_bradcrack_data(bravais):
    r
    json_file = pkg_resources.resource_filename(__name__, 'bradcrack.json')
    with open(json_file, 'r') as f:
        bradcrack_data = load_json(f)
        return bradcrack_data[bravais]