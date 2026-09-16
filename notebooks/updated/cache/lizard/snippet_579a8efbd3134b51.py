def survey_loader(sur_dir=SUR_DIR, sur_file=SUR_FILE):
    survey_path = os.path.join(sur_dir, sur_file)
    survey = None
    with open(survey_path) as survey_file:
        survey = Survey(survey_file.read())
    return survey