def unique_categories(categories):
    categories = np.unique(categories)
    categories = np.setdiff1d(categories, np.array(settings.
        categories_to_ignore))
    categories = np.array(natsorted(categories, key=lambda v: v.upper()))
    return categories