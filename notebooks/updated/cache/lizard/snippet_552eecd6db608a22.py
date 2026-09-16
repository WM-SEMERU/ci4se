def prepare(cls):
    if cls._ask_openapi():
        napp_path = Path()
        tpl_path = SKEL_PATH / 'napp-structure/username/napp'
        OpenAPI(napp_path, tpl_path).render_template()
        print('Please, update your openapi.yml file.')
        sys.exit()