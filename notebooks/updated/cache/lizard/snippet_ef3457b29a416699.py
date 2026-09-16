def is_cython(obj):

    def check_cython(x):
        return type(x).__name__ == 'cython_function_or_method'
    return check_cython(obj) or hasattr(obj, '__func__') and check_cython(obj
        .__func__)