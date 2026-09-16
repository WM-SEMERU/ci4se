def load_apis(self, path, ignore=[], include_crash_api=False):
    if not path:
        raise Exception('Missing path to api swagger files')
    if type(ignore) is not list:
        raise Exception("'ignore' should be a list of api names")
    ignore.append('pym-config')
    apis = {}
    log.debug('Searching path %s' % path)
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith('.yaml'):
                api_name = f.replace('.yaml', '')
                if api_name in ignore:
                    log.info('Ignoring api %s' % api_name)
                    continue
                apis[api_name] = os.path.join(path, f)
                log.debug('Found api %s in %s' % (api_name, f))
    for name in ['ping', 'crash']:
        yaml_path = pkg_resources.resource_filename(__name__, 
            'pymacaron/%s.yaml' % name)
        if not os.path.isfile(yaml_path):
            yaml_path = os.path.join(os.path.dirname(sys.modules[__name__].
                __file__), '%s.yaml' % name)
        apis[name] = yaml_path
    if not include_crash_api:
        del apis['crash']
    self.path_apis = path
    self.apis = apis
    return self