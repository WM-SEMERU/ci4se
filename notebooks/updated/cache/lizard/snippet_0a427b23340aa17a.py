def startup(api=None):

    def startup_wrapper(startup_function):
        apply_to_api = hug.API(api) if api else hug.api.from_object(
            startup_function)
        apply_to_api.add_startup_handler(startup_function)
        return startup_function
    return startup_wrapper