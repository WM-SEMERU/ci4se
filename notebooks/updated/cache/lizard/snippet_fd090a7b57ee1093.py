def __getJoin(self, web):
    join = web.findAll('a', {'class': 'dropdown-item'})
    for j in join:
        try:
            if 'Joined GitHub' in j.text:
                self.join = j['href'][-10:]
        except IndexError as error:
            print('There was an error with the user ' + self.name)
            print(error)
        except AttributeError as error:
            print('There was an error with the user ' + self.name)
            print(error)