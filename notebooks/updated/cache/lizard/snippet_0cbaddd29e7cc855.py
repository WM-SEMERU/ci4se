def start_tpot(automated_run, session, path):
    module = functions.import_string_code_as_module(automated_run.source)
    extraction = session.query(models.Extraction).first()
    X, y = extraction.return_train_dataset()
    tpot_learner = module.tpot_learner
    tpot_learner.fit(X, y)
    temp_filename = os.path.join(path, 'tpot-temp-export-{}'.format(os.
        getpid()))
    tpot_learner.export(temp_filename)
    with open(temp_filename) as f:
        base_learner_source = f.read()
    base_learner_source = (constants.tpot_learner_docstring +
        base_learner_source)
    try:
        os.remove(temp_filename)
    except OSError:
        pass
    blo = models.BaseLearnerOrigin(source=base_learner_source, name=
        'TPOT Learner', meta_feature_generator='predict')
    session.add(blo)
    session.commit()