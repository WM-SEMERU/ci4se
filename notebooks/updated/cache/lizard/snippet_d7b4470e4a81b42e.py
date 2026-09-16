def preprocess_points(points, preprocessor):
    try:
        points = preprocessor(points)
    except Exception as e:
        raise PreprocessorError(e)
    return points