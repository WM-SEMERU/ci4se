def load(filename):
    json_obj = Seed.load(filename)
    return SeedInteger(json_obj['seed_value'], json_obj['seed_id'],
        json_obj['date'])