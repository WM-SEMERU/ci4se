def __get_all_scrapers_modules(self):
    modules = []
    file = os.path.realpath(__file__)
    folder = os.path.dirname(file)
    for filename in os.listdir(folder + '/../scrapers'):
        if filename.endswith('Scraper.py') and not filename.startswith('Base'):
            modules.append(filename[:-3])
    return modules