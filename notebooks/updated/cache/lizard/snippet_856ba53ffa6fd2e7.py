def get_models():
    all_models = gfile.Glob(os.path.join(models_dir(), '*.meta'))
    model_filenames = [os.path.basename(m) for m in all_models]
    model_numbers_names = sorted([(shipname.detect_model_num(m), shipname.
        detect_model_name(m)) for m in model_filenames])
    return model_numbers_names