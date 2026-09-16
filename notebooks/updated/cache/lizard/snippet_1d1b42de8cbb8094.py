def dump(obj, fp, **user_kwargs):
    return json.dump(obj, fp, **_encoder_kwargs(user_kwargs))