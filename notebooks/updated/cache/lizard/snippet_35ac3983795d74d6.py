def plugin_categories_to_choices(categories):
    choices = []
    for category, items in categories.items():
        if items:
            plugin_tuples = tuple((plugin.type_name, plugin.verbose_name) for
                plugin in items)
            if category:
                choices.append((category, plugin_tuples))
            else:
                choices += plugin_tuples
    choices.sort(key=lambda item: item[0])
    return choices