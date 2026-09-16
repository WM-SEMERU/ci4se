def run_getmy(filename, **kwargs):
    assume_yes = kwargs.get('yes_to_all')
    user = getenv('GETGIST_USER')
    getgist = GetGist(user=user, filename=filename, assume_yes=assume_yes)
    getgist.get()