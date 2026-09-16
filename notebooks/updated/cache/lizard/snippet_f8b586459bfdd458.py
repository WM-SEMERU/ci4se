def create_script(create=None):
    if connexion.request.is_json:
        create = Create.from_dict(connexion.request.get_json())
    if not hasAccess():
        return redirectUnauthorized()
    driver = LoadedDrivers.getDefaultDriver()
    driver.saveScript(create.script.name, create.script.content)
    return Response(status=200, body={'file-name': create.script.name})