def get_switch_actors(self):
    actors = {}
    for ain in self.homeautoswitch('getswitchlist').split(','):
        actors[ain] = {'name': self.homeautoswitch('getswitchname', ain),
            'state': bool(self.homeautoswitch('getswitchstate', ain)),
            'present': bool(self.homeautoswitch('getswitchpresent', ain)),
            'power': self.homeautoswitch('getswitchpower', ain), 'energy':
            self.homeautoswitch('getswitchenergy', ain), 'temperature':
            self.homeautoswitch('getswitchtemperature', ain)}
    return actors