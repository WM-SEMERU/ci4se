def rename_categories(self, new_categories, inplace=False):
    inplace = validate_bool_kwarg(inplace, 'inplace')
    cat = self if inplace else self.copy()
    if isinstance(new_categories, ABCSeries):
        msg = """Treating Series 'new_categories' as a list-like and using the values. In a future version, 'rename_categories' will treat Series like a dictionary.
For dict-like, use 'new_categories.to_dict()'
For list-like, use 'new_categories.values'."""
        warn(msg, FutureWarning, stacklevel=2)
        new_categories = list(new_categories)
    if is_dict_like(new_categories):
        cat.categories = [new_categories.get(item, item) for item in cat.
            categories]
    elif callable(new_categories):
        cat.categories = [new_categories(item) for item in cat.categories]
    else:
        cat.categories = new_categories
    if not inplace:
        return cat