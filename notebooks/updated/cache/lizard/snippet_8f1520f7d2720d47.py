def rename_script(rename=None):
    if connexion.request.is_json:
        rename = Rename.from_dict(connexion.request.get_json())
    return 'do some magic!'