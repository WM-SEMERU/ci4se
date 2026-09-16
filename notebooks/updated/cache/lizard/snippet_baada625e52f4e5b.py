def download(model, direct=False, *pip_args):
    dl_tpl = '{m}-{v}/{m}-{v}.tar.gz#egg={m}=={v}'
    if direct:
        components = model.split('-')
        model_name = ''.join(components[:-1])
        version = components[-1]
        dl = download_model(dl_tpl.format(m=model_name, v=version), pip_args)
    else:
        shortcuts = get_json(about.__shortcuts__, 'available shortcuts')
        model_name = shortcuts.get(model, model)
        compatibility = get_compatibility()
        version = get_version(model_name, compatibility)
        dl = download_model(dl_tpl.format(m=model_name, v=version), pip_args)
        if dl != 0:
            sys.exit(dl)
        msg.good('Download and installation successful',
            "You can now load the model via spacy.load('{}')".format(
            model_name))
        if model in shortcuts:
            try:
                package_path = get_package_path(model_name)
                link(model_name, model, force=True, model_path=package_path)
            except:
                msg.warn('Download successful but linking failed',
                    "Creating a shortcut link for '{}' didn't work (maybe you don't have admin permissions?), but you can still load the model via its full package name: nlp = spacy.load('{}')"
                    .format(model, model_name))