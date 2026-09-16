def delete_script(delete=None):
    if connexion.request.is_json:
        delete = Delete.from_dict(connexion.request.get_json())
    if not hasAccess():
        return redirectUnauthorized()
    driver = LoadedDrivers.getDefaultDriver()
    driver.deleteScript(delete.script.name)
    return Response(status=200, body={})