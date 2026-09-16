def jsonresolver_loader(url_map):
    from flask import current_app
    from . import current_jsonschemas
    url_map.add(Rule('{0}/<path:path>'.format(current_app.config[
        'JSONSCHEMAS_ENDPOINT']), endpoint=current_jsonschemas.get_schema,
        host=current_app.config['JSONSCHEMAS_HOST']))