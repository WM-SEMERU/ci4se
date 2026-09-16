def __getLocation(self, web):
    try:
        self.location = web.find('span', {'class': 'p-label'}).text
    except AttributeError as error:
        print('There was an error with the user ' + self.name)
        print(error)