def generate_training_command(model_folder):
    update_if_outdated(model_folder)
    model_description_file = os.path.join(model_folder, 'info.yml')
    with open(model_description_file, 'r') as ymlfile:
        model_description = yaml.load(ymlfile)
    project_root = utils.get_project_root()
    data = {}
    data['training'] = os.path.join(project_root, model_description[
        'data-source'], 'traindata.hdf5')
    data['testing'] = os.path.join(project_root, model_description[
        'data-source'], 'testdata.hdf5')
    data['validating'] = os.path.join(project_root, model_description[
        'data-source'], 'validdata.hdf5')
    basename = 'model'
    latest_model = utils.get_latest_working_model(model_folder)
    if latest_model == '':
        logging.error("There is no model with basename '%s'.", basename)
        return None
    else:
        logging.info("Model '%s' found.", latest_model)
        i = int(latest_model.split('-')[-1].split('.')[0])
        model_src = os.path.join(model_folder, '%s-%i.json' % (basename, i))
        model_target = os.path.join(model_folder, '%s-%i.json' % (basename,
            i + 1))
    training = model_description['training']
    training = training.replace('{{testing}}', data['testing'])
    training = training.replace('{{training}}', data['training'])
    training = training.replace('{{validation}}', data['validating'])
    training = training.replace('{{src_model}}', model_src)
    training = training.replace('{{target_model}}', model_target)
    training = training.replace('{{nntoolkit}}', utils.get_nntoolkit())
    return training