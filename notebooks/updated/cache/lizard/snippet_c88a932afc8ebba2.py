def configure(obj, token):
    config = obj.get('config') or FileConfig(obj['profile'])
    config.auth_token = token
    config.save()