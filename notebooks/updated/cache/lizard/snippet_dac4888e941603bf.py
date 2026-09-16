def index(objects, attr):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        return {getattr(obj, attr): obj for obj in objects}