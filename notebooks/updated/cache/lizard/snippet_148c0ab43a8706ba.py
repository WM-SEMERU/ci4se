def return_main_dataset(self):
    if not self.main_dataset['source']:
        raise exceptions.UserError('Source is empty')
    extraction_code = self.main_dataset['source']
    extraction_function = functions.import_object_from_string_code(
        extraction_code, 'extract_main_dataset')
    try:
        X, y = extraction_function()
    except Exception as e:
        raise exceptions.UserError('User code exception', exception_message
            =str(e))
    X, y = np.array(X), np.array(y)
    return X, y